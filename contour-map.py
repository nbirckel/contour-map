
import pygmt
from datetime import datetime
now = datetime.now() # current date and time
date = now.strftime("%Y%m%d_%H%M")
title = "Chaine des Puys"
coords =[2.5,3.5,44,46]
grid = pygmt.datasets.load_earth_relief(resolution="01m", region=coords)
fig = pygmt.Figure()
pygmt.config(PS_PAGE_COLOR="#fcf0e9")
fig.grdcontour(
    grid=grid,
    projection='M8i',
    interval=100,
    limit=[0, 5000],
    frame=False,
    pen='0.5p,#484163',
)
fig.text(
text=title,
x=3,
y=44.10,
font="48p,Helvetica-Bold,#484163",
)
fig.text(
text="SRTM data from pygmt | Code & Design by Nicolas Birckel",
x=3,
y=44.06,
font="12p,Helvetica-Bold,#484163",
)
filename = date+"_"+title+"_contour.png"
fig.savefig(filename)
