d3.xml('/wordcloud').then(data => {
    d3.select('#svg-container').node().append(data.documentElement);
    d3.selectAll('#svg-container text').data(function (data, idx, elem) {
        console.log(this);
        console.log(data);
        console.log(idx);
        console.log(elem);
    });
    // d3.selectAll('#svg-container text')
    //     .on('mouseover', function(data, idx, elem) {
    //         console.log(elem);
    //     });
});
