## Sample XML

Below is a sample XML document that validates against the Example
Extension described in this Appendix:

&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;msg:Message xmlns:xmp="http://www.fixm.aero/ext/example/1.0"
xmlns:fx="http://www.fixm.aero/flight/4.2"
xmlns:fb="http://www.fixm.aero/base/4.2"
xmlns:msg="http://www.fixm.aero/app/msg/1.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;

&lt;msg:extension xsi:type="xmp:ExampleMessageType"&gt;

&lt;xmp:sequenceNumber&gt;1903&lt;/xmp:sequenceNumber&gt;

&lt;/msg:extension&gt;

&lt;msg:flight&gt;

&lt;fx:enRoute&gt;

&lt;fx:extension xsi:type="xmp:ExampleEnRouteType"&gt;

&lt;xmp:position srsName="urn:ogc:def:crs:EPSG::4326"&gt;

&lt;fb:pos&gt;36.019970 -75.668760&lt;/fb:pos&gt;

&lt;/xmp:position&gt;

&lt;/fx:extension&gt;

&lt;/fx:enRoute&gt;

&lt;/msg:flight&gt;

&lt;/msg:Message&gt;

**Rulebook**

Versioning & namespace

-   An Extension should employ semantic versioning (major.minor.micro)
    with version number starting at 1.0.0.

-   ...

Diagrams

-   Include copyright notice in each model diagram

Naming

-   Name characters limited to upper and lower case, digits and
    underscore

-   Use InterCap notation (= “Camel Case”) for all model elements

-   Use starting capital for packages and classes

-   Use starting miniscule for attributes and roles

-   Use all capitals for enumeration values

-   Names should be expressive of data content or relationship

-   Names should not be of unwieldy length

Inheritance

-   Abstract classes are allowed

-   Root classes are forbidden

-   Leaf classes must be justified

Datatypes

-   ...

Stereotypes

-   ...

**Creating an Extension step by step**


