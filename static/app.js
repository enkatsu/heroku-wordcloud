d3.json('/api/wordcloud')
  .then(data => {
    console.log(data);
    d3.select('div.loader-inner.ball-pulse').remove();
    const svg = d3.select('svg#svg-container');
    svg.attr('width', data.width).attr('height', data.height);
    svg.selectAll('text')
      .data(data.words)
      .enter()
      .append('text')
      .text(d => d.text)
      .attr('style', d => d.style)
      .attr('font-size', d => d.font_size)
      .attr('transform', d => d.transform)
      .style('cursor', 'pointer')
      .on('mouseover', function(d, i, elm) {
        d3.select(this).attr('font-size', 100);
      })
      .on('mouseout', function(d, i, elm) {
        d3.select(this).attr('font-size', d.font_size);
      });
  })
  .catch(err => {
    console.log(err);
    alert('Error');
  });
