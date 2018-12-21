const table = document.getElementsByTagName('table')[0];
reportData = reportData.sort((a, b) => {
    if (a.date < b.date) return -1
    if (a.date > b.date) return 1
});
let sumHours = 0;
reportData.forEach((record) => {
    const tr = document.createElement('tr')

    const tdDate = createTdElementWithText(record.date);
    tr.appendChild(tdDate);

    const tdLoggedTime = createTdElementWithText(record.loggedTime);
    tr.appendChild(tdLoggedTime);

    const tdCardId = createTdElementWithText(record.cardId);
    tr.appendChild(tdCardId);

    const tdCardTitle = createTdElementWithText(record.cardTitle);
    tr.appendChild(tdCardTitle);

    table.appendChild(tr);

    sumHours += parseFloat(record.loggedTime);
})

const trSum = document.createElement('tr');

const tdTotal = createTdElementWithText('Total: ');
trSum.appendChild(tdTotal);

const tdHours = createTdElementWithText(sumHours);
trSum.appendChild(tdHours);

table.appendChild(trSum);

function createTdElementWithText(text) {
    const element = document.createElement('td');
    const textNode = document.createTextNode(text);
    element.appendChild(textNode);
    return element;
}
