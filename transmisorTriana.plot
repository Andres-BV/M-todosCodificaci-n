set term postscript eps color 10
set view map
set pm3d map
set cbrange[0:100]
set xlabel 'Word length (power of 2)'
set ylabel 'Frequency of zeroes'
set title 'Avg. prob. of correct transmission'
set output "canalTriana.eps"
set palette color positive
set key off
set size square
set yrange [0.05:0.95]
set xrange [-0.75:9.75]
set xtics 0, 1
set ytics 0.1, 0.1
splot "canalTriana.dat" using ($1-0.5):($2+0.05):($3*100.0)
