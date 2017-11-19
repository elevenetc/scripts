function calcMem(rangeValue) {

    var sheet = SpreadsheetApp.getActiveSpreadsheet();

    if (sheet.getRange(rangeValue).isBlank()) return;

    var repeatColor = '#ffeca8';
    var workedColor = '#d6f9ca';
    var emptyColor = '#ffffff';


    var row = sheet.getRange(rangeValue);
    var cellsCount = row.getWidth();
    var aCount = 0;
    var bCount = 0;
    var cCount = 0;
    var weigth = 0;

    var backs = row.getBackgrounds();
    var values = row.getValues();

    for (c = cellsCount - 1; c >= 0; c--) {
        var cell = row.getCell(1, c + 1);
        var value = values[0][c];

        if (value === 'A') aCount++;
        else if (value === 'B') bCount++;
        else if (value === 'C') cCount++;

        if (!cell.isBlank()) {
            backs[0][c] = workedColor
        } else {
            backs[0][c] = emptyColor
        }
    }

    weight = Math.ceil(aCount - bCount / 2 - cCount);

    for (c = cellsCount - 1; c >= 0; c--) {
        var cell = row.getCell(1, c + 1);

        if (!cell.isBlank()) {

            var value = values[0][c];
            var repeatCell = -10000;

            if (value === 'C') {
                repeatCell = c + 1
            } else if (value === 'B') {
                repeatCell = c + 2 + weight
            } else if (value === 'A') {
                repeatCell = c + 3 + weight
            }

            if (repeatCell !== -10000) {
                if (repeatCell <= c) repeatCell = c + 1;
                backs[0][repeatCell] = repeatColor
            }

            break;
        }
    }

    sheet.getRange(rangeValue).setBackgrounds(backs)
}

function test() {
    var testRow = 33;
    calcMem('G' + testRow + ':BQ' + testRow)
}

function fillAll() {
    for (var i = 6; i <= 143; i++) {
        var range = 'G' + i + ':BQ' + i;
        calcMem(range)
    }
}

function onEdit(e) {
    var sheet = SpreadsheetApp.getActiveSheet()
    var activeCell = sheet.getActiveCell()
    var col = activeCell.getColumn()
    var row = activeCell.getRow()
    var range = 'G' + row + ':BQ' + row
    calcMem(range)
}