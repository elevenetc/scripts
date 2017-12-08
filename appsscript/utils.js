/**
 * Accepts instance of Date
 */
function sameDay(d1, d2) {
    if (!(d1 instanceof Date) || !(d2 instanceof Date)) throw 'dates should be instance of Date, but was d1: ' + d1 + ' d2: ' + d2

    return d1.getFullYear() === d2.getFullYear() &&
        d1.getMonth() === d2.getMonth() &&
        d1.getDate() === d2.getDate()
}

/**
 * Returns index of column from row range
 *
 * @param datesRange is String like 'A1:A100'
 */
function getCurrentDateCol(datesRange) {

    var sheet = SpreadsheetApp.getActiveSpreadsheet();
    var currentDate = new Date();
    var datesRow = sheet.getRange(datesRange);
    var datesValues = datesRow.getValues()[0];
    var count = datesRow.getWidth();
    for (var d = 0; d < count; d++) {
        var date = datesValues[d];
        if (!(date instanceof Date)) continue;//if cell is not filled with data

        if (sameDay(date, currentDate)) {
            return d
        }
    }
    return -1
}

function fillRangeBackground(range, color) {
    var sheet = SpreadsheetApp.getActiveSpreadsheet();
    var row = sheet.getRange(datesRange);
    var backgrounds = row.getBackgrounds();
    for (var i = 0; i < backgrounds.length; i++) {
        backgrounds[0][i] = color;
    }
    sheet.getRange(range).setBackgrounds(backgrounds);
}

function isGroupTopicRow(rowIndex) {
    var sheet = SpreadsheetApp.getActiveSpreadsheet();
    var row = sheet.getRange(topicGroupCol + '' + rowIndex);
    return !row.isBlank()
}