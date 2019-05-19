var pager = new ETNGpager('requirements.txt', 'list2', 24, 10);
var curP = 1;
page();

function page(i) {
    curP = (curP > pager.cntP) ? 1 : curP;
    if (i) {
        curP = n = i;
    } else {
        n = curP++;
    }
    pager.curP = (n > pager.cntP) ? pager.cntP : n;
    pager.create();
}