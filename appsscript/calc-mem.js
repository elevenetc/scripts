var topRow = 6;
var bottomRow = 159;
var leftCol = 'G';
var rightCol = 'BQ';
var datesRange = 'G4:BQ4';

var repeatColor = '#ffeca8';
var repeatAfterFailColor = '#FF8E00';
var workedColor = '#d6f9ca';
var emptyColor = '#ffffff';
var deadlineColor = '#ff0000';

function calcMem(rangeValue, row) {

    if(isGroupTopicRow(row)) return;

    var sheet = SpreadsheetApp.getActiveSpreadsheet();
    var isEmpty = sheet.getRange(rangeValue).isBlank();

    var row = sheet.getRange(rangeValue);
    var cellsCount = row.getWidth();
    var aCount = 0;
    var bCount = 0;
    var cCount = 0;
    var weigth = 0;

    var backs = row.getBackgrounds();
    var values = row.getValues();

    var currentDateCell = getCurrentDateCol(datesRange);
    var deadlined = false;

    if(isEmpty) {
        for (var i = 0; i <= currentDateCell; i++) {
            backs[0][i] = deadlineColor
        }
    } else {
        for (var c = cellsCount - 1; c >= 0; c--) {
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

        var repeatCell;
        var lastWorkedCell;

        for (c = cellsCount - 1; c >= 0; c--) {//find last filled cell
            var cell = row.getCell(1, c + 1);

            if (!cell.isBlank()) {


                var value = values[0][c];
                var lastIsFailed = false;

                if (value === 'C') {
                    repeatCell = c + 1;
                    lastIsFailed = true;
                } else if (value === 'B') {
                    repeatCell = c + 2 + weight;
                } else if (value === 'A') {
                    repeatCell = c + 3 + weight;
                } else {
                    //invalid value
                    continue;
                }

                if (repeatCell <= c) repeatCell = c + 1;
                backs[0][repeatCell] = lastIsFailed ? repeatAfterFailColor : repeatColor;

                deadlined = repeatCell < currentDateCell;
                lastWorkedCell = c;

                break;
            }
        }

        if (deadlined) {
            for (var i = lastWorkedCell + 1; i <= currentDateCell; i++) {
                backs[0][i] = deadlineColor
            }
        }
    }

    sheet.getRange(rangeValue).setBackgrounds(backs);
}

function test() {
    calcMem(leftCol + topRow + ':' + rightCol + topRow, topRow)
}

function fillAll() {
    fill(topRow, bottomRow, leftCol, rightCol);
}

function getLastTopicRow(){
    var sheet = SpreadsheetApp.getActiveSheet();
    var topicsCol = sheet.getRange('B5:B');
    var topics = topicsCol.getValues();
    for(var i = topics.length - 1; i >= 0; i--){
        if(topics[i][0] != ''){
            return i;
        }
    }
    return -1;
}

function fill(top, bottom, left, right){
    for (var r = top; r <= bottom; r++) {
        var range = left + r + ':' + right + r;
        calcMem(range, r)
    }
}

function onEdit(e) {
    var sheet = SpreadsheetApp.getActiveSheet();
    var activeCell = sheet.getActiveCell();
    var row = activeCell.getRow();
    var range = leftCol + row + ':' + rightCol + row;
    calcMem(range, row)
}

function onOpen(e) {
    var lastTopicRow = getLastTopicRow()
    if(lastTopicRow != -1){
        fill(topRow, lastTopicRow + 4, leftCol, rightCol);
    }
}
