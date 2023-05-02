# paleo-atlantic-ocean-sections

## Summary of program process
This program reads in and combines two sediment core stable isotope databases. It then automates data cleaning and wrangling to filter for the desired geographic location of sediment cores (focused on the Atlantic Ocean), splices the data set by specified age ranges, calculates a mean stable isotope value for each sediment core within a given age range, and returns a finalized MultiIndex data set. Lastly, the program develops a detailed figure, showing stable isotope values throughout the Atlantic Ocean for each age range.

Both .csv files must be in the same folder as atlantic_d13C_sections.py in order for program to run. If trouble running, check out the included .png file for the final program figure output.

## Background
The deep ocean (>1000 m) is home to a conveyor belt of ocean water masses, which play a central role in transporting heat, nutrients, and carbon throughout the world’s oceans. Because the ocean conveyor belt is driven by differences in water density, input of relatively buoyant fresh meltwater from the polar icecaps can disrupt this circulation, thereby significantly impacting Earth’s climate system.

Comparison of water mass circulation throughout Earth’s past can help to answer questions about the interconnectedness of climate and ocean circulation. For example, during the Last Glacial Maximum (about 20,000 year ago) when global atmospheric CO2 values were 100 ppm lower than preindustrial levels, where exactly did all of that carbon disappear to?

Today, direct measurements of seawater at various depths and locations can be used to construct visuals of modern deep ocean water mass circulation. But how do we learn about the Last Glacial Maximum when we can’t take direct measurements of water from 20,000 years ago? Instead, we must rely on chemical tracers of water masses, recorded by the isotopic composition of foraminiferal shells. 

Foraminifera are single-celled organisms that build tiny sand sized shells which reflect the chemical composition of the water in which they live. When foraminifera die, their shells fall through the water column and are deposited on the sea floor where they accumulate over time. Sediment cores stretching meters long can capture hundreds of thousands to millions of years of this sedimentation history.

In this program, I work with an incredible data set of sediment core carbon isotope records compiled by Oliver et al (2010), which when viewed together, help to paint a picture of water mass circulation throughout the world’s oceans. Focusing in on the Atlantic Ocean, I generate ocean cross sections for six distinct time periods throughout Earth’s past. The left column are all relatively warm periods, similar to the modern climate. The right column are relatively cold glacial periods. 

There are many takeaways from this comparison but let’s focus on one that helps to answer our question from before. Back during the Last Glacial Maximum, when atmospheric CO2 values were 100 ppm lower than preindustrial levels, where exactly did all of that carbon go? Look no further than the deep ocean! During glacial periods (right column), blue values below 2500 meters water depth indicate immense storage of isotopically light carbon in the depths of the abyssal ocean. During interglacial periods (left column) that reservoir becomes much smaller. This is just one example of the significant interconnectedness of Earth’s climate with deep ocean circulation. However, this in no way explains the unprecedented modern atmospheric CO2 levels. It merely offers insight into the natural glacial-interglacial climate oscillation observed prior to the industrial revolution.

I am contruting this analysis to a publication, currently under review in *Paleoceanography*.

Citation for Oliver et al (2010) data set:  
Oliver, K. I. C., Hoogakker, B. A. A., Crowhurst, S., Henderson, G. M., Rickaby, R. E. M., Edwards, N. R., & Elderfield, H. (2010). A synthesis of marine sediment core δ13C data over the last 150 000 years. Climate of the Past, 6(5), 645–673. https://doi.org/10.5194/cp- 6-645-2010

## Required packages
- numpy
- pandas
- matplotlib.pyplot
- matplotlib.transforms
- matplotlib.cm
- matplotlib.colors
- seaborn

