## FIXM Samples of 4DT Data

A key component of FIXM is the ability to express a four-dimensional
trajectory (4DT). Since no 4DTs are available in sample ATS messages, a
small set of data representing 4DTs for three flights was converted to
FIXM. This set was comprised of three “Creation Request” messages. These
were used to create “Electronic Flight Plan” (eFPL) messages, which
correspond to converted FPL messages with 4DT data merged into them. The
4DT data includes climb profile, descent profile, and desired
trajectory. The trajectory data includes position, time, altitude,
speed, and weather data associated with each trajectory element.

The FIXM data was generated using both the provided 4DT data and the
route text, parsed into route elements, and merged together into a
logical sequence. However, not every 4DT point corresponded to a route
element, and not every route element had a corresponding 4DT data point.
As a result, the FIXM trajectory contains a logical sequence of
trajectory elements, with some of the trajectory elements containing
associated 4DT data and some not. While this may not represent how an
ideal 4DT message would appear if originally generated in FIXM format,
it does produce a logical result that is FIXM compliant.


