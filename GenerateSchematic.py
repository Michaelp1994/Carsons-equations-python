import schemdraw
import matplotlib

import schemdraw.elements as elm
from schemdraw.segments import *


class LightningBolt(elm.Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment([(0, 0), (0.3, 0.5)], arrow="<-"))
        self.segments.append(Segment([(0.3, 0.5), (0, 0.5)]))
        self.segments.append(Segment([(0, 0.5), (0.3, 1)]))


def unit(name, resistance, current):
    d = schemdraw.Drawing(show=False)
    d += elm.Line()
    d += elm.CurrentLabelInline(length=1.25, reverse=True).label("%iA" % current)
    d += elm.Dot()
    d.push()
    d += elm.Line().down()
    d += elm.CurrentLabelInline(length=1.25).label("%iA" % current)
    d += (
        elm.Ground()
        .label(name, loc="bottom")
        .label("RAT = %i Ω" % resistance, loc="bottom", ofst=0.5)
    )
    d.pop()
    return d


with schemdraw.Drawing(show=True) as d2:
    d2.push()
    d2 += elm.Line().down()
    d2 += elm.CurrentLabelInline(length=1.25).label("5A")
    d2 += (
        elm.Ground()
        .label("SE TOY", loc="bottom")
        .label("RAT = 0.5 Ω", loc="bottom", ofst=0.5)
    )
    d2.pop()
    d2 += elm.Line().length(d2.unit / 6)
    d2 += elm.DotDotDot()
    d2 += elm.Line().length(d2.unit / 6)

    for i in range(1, 4):
        d2 += elm.ElementDrawing(unit("T%i" % i, i, i * 10))
    d2 += LightningBolt()

    d2 += elm.Line().length(d2.unit / 6)
    d2 += elm.DotDotDot()
    d2 += elm.Line().length(d2.unit / 6)

    d2.push()
    d2 += elm.Line().down()
    d2 += elm.CurrentLabelInline(length=1.25).label("5A")
    d2 += (
        elm.Ground()
        .label("SE ESO", loc="bottom")
        .label("RAT = 0.5 Ω", loc="bottom", ofst=0.5)
    )
    d2.pop()
    # d += elm.Line().label("95A")
    # d += elm.Dot()
    # d.push()
    # d += elm.Resistor().down().label("T2", loc="bottom")
    # d += elm.Ground()

d2.draw()
