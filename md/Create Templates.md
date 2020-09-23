## Create Templates

FIXM is a general-purpose standard meant to facilitate the exchange of
any and all flight data. To accomplish this, it must be extremely
flexible in terms of required data content. However, individual users of
the FIXM standard may want to lockdown the expected format of their data
to reflect the content requirements of their particular message
exchanges. Message templates, created via XSD restrictions, is the
current method recommended by FIXM to accomplish this goal. For this
example, we will create two templates to illustrate the process:
departure alerts and arrival alerts.

### Create an Overall Template Container

The steps for creating this package are largely identical to those
outlined in [Create an Application
Package](#create-an-application-package) above. Key differences are
noted below.

1.  Begin by right clicking on your Application package and choose “Add
    a Package…”.

<img src=".//media/image99.png" style="width:4.16in;height:5.04in" />

1.  In the New Package dialogue box, change the *Name* field to
    something appropriate to your templates (here we used
    “ExampleTemplates”), select the *Package Only* radio button, and
    then click OK.

<img src=".//media/image100.png" style="width:3.70885in;height:2.97958in" />

1.  Apply a schema stereotype and begin setting up schema properties as
    outlined in [Apply Schema Stereotype](#apply-schema-stereotype) and
    [Set Up Schema Properties](#set-up-schema-properties) above using
    the same *Target Namespace* and *Prefix* as was used for your
    Application package[24].

<img src=".//media/image101.png" style="width:5.21948in;height:3.39631in" />

1.  For the *Schema File* field, choose something appropriate for your
    templates (in this example,
    “.\\schemas\\applications\\examplemessage\\exampletemplates\\ExampleTemplates.xsd”).
    Please note, you will want to create a new subdirectory under your
    Application’s directory to hold the templates (in this example,
    “exampletemplates” should be created below the “examplemessage”
    directory).

<img src=".//media/image102.png" style="width:2.03153in;height:0.7501in" />

1.  In some cases, Sparx EA will automatically add additional namespace
    prefixes for packages that need to be imported, but that does not
    happen in this instance. Address this by manually adding the
    namespaces of any packages you will import. This step is
    accomplished by:

<!-- -->

1.  Clicking “New” to open a Namespace Details dialogue box.

2.  Filling in appropriate details for each namespace to be included.

3.  Then clicking OK.

> In this example, our templates will import Base and Flight from Core.
> See below for examples showing how each Namespace Details dialogue box
> should be filled in.
>
> <img src=".//media/image103.png" style="width:4.1985in;height:1.50021in" />
>
> <img src=".//media/image104.png" style="width:4.14641in;height:1.46895in" />

1.  At this point, your XSD schema Properties dialogue box should look
    something like below. Click OK to save these settings.

<img src=".//media/image105.png" style="width:5.17781in;height:3.39631in" />

1.  Finally, follow the steps outlined in [Add Schema Description and
    Tags](#add-schema-description-and-tags) to complete the setup of
    your template container.

### Create a Container for each Type of Message Template

With the overall template container built, you must now create
individual containers for each message template you wish to include in
your exchange. In this example, we will create two such containers:
ArrivalAlert and DepartureAlert. Due to their similarity in structure to
the overall container, we can use a shortcut to build them rather than
repeating all the steps from the previous section.

1.  Right click on your newly created template container in Project
    Browser and choose “Copy / Paste” and then “Copy to Clipboard” and
    then “Full Structure of Duplication”.

<img src=".//media/image106.png" style="width:6.5in;height:4.56736in" />

1.  Once again, right click on your template container in Project
    Browser and this time choose “Copy / Paste” and then “Paste Package
    from Clipboard”.

<img src=".//media/image107.png" style="width:6.5in;height:5.73333in" />

1.  You should see a new copy of your container show up in Project
    Browser below the original.

<img src=".//media/image108.png" style="width:3.37547in;height:5.06321in" />

1.  Repeat the above “Paste Package from Clipboard” step for each
    message template you would like to create[25]. In this example, we
    will create two message templates. When finished, your Project
    Browser should display something similar to below.

<img src=".//media/image109.png" style="width:3.7922in;height:5.06321in" />

1.  Double click (or right click and choose “Properties…”) on each
    individual message template container and modify the *Schema Name*
    and *Schema File* fields to be something appropriate for your
    templates. Outside of Sparx EA, you will also want to create
    individual directories below the overall template directory to hold
    each message template. For this example, the following values should
    be used:

    1.  ArrivalAlert template

        1.  *Schema Name* set to: “ArrivalAlert”

        2.  *Schema File* set to:
            > “.\\schemas\\applications\\examplemessage\\exampletemplates\\arrivalalert\\ArrivalAlert.xsd”

    2.  DepartureAlert template

        1.  *Schema Name* set to: “DepartureAlert”

        2.  *Schema File* set to:
            > “.\\schemas\\applications\\examplemessage\\exampletemplates\\departurealert\\DepartureAlert.xsd”

> And the schemas directory structure should be modified as follows:

<img src=".//media/image110.png" style="width:2.05237in;height:1.10432in" />

> Don’t forget to modify your schema descriptions to something
> appropriate as well. In this example, ArrivalAlert should use “An
> example Arrival Alert template.” and DepartureAlert should use “An
> example Departure Alert template”.

1.  When finished, your Project Browser should display something similar
    to below.

<img src=".//media/image111.png" style="width:3.41714in;height:5.02153in" />

### Create a Message Template

The individual message templates themselves recreate the structure of
the portions of the models that they draw fields from and reuse the same
namespaces, prefixes, and package names. They use different diagram
names, schema file names, schema descriptions, and, of course, the
content itself is modified using XSD restrictions.

The convention used so far in FIXM when naming template material is to
prefix the existing names with text to identify the Application followed
by text to identify the particular message. So, for this example, fields
under ArrivalAlert will be prefixed with “ExampleAA\_” while fields
under DepartureAlert will be prefixed with “ExampleDA\_”.

#### Create Template Packages

One template package will need to be created for each Core or
Application package you wish to restrict. So, for this example, the
ArrivalAlert template will need to create an ExampleMessage package, a
Flight package, an Arrival package, and a FlightData package because
these are the packages that will be restricted to create an ArrivalAlert
message.

These template packages should replicate all the settings of the package
they correspond to except for their diagram’s *Name* field (if they have
an associated diagram – some packages won’t), the schema description,
and the *Schema File* field of their schema properties.

1.  Follow the steps outlined in [Create an Application
    Package](#create-an-application-package) to recreate, under your
    message template container, the packages you wish to restrict in
    your template. All names, properties, descriptions, tags, etc.,
    should be the same[26] except:

    1.  If your package has an associated diagram, change the diagram
        *Name* to include your template’s prefix. While not strictly
        necessary, this helps prevent confusing template diagrams with
        the originals.

    2.  Change the *Schema File* field to use a path corresponding to
        your message template and a filename beginning with your
        template’s prefix. Template schema files should be located under
        the directory of your message container but their paths should
        otherwise include creating any intermediate directories, etc.,
        so that they are structured similar to the paths to the files
        they are restricting.

    3.  Indicate that the schema is a template in the description text.

For this example, we will first create a template package corresponding
to ExampleMessage under ArrivalAlert. When creating the package, we will
change its diagram name to be “ExampleAA\_ExampleMessage”.

<img src=".//media/image112.png" style="width:6.5in;height:4.81736in" />

<img src=".//media/image113.png" style="width:3.6776in;height:5.05279in" />

When configuring the package, use all the same values as ExampleMessage
except change the schema description to “An example Arrival Alert
message template for the ExampleMessage package.” and the *Schema File*
field to
“.\\schemas\\applications\\examplemessage\\exampletemplates\\arrivalalert\\examplemessage\\ExampleAA\_ExampleMessage.xsd”.

<img src=".//media/image114.png" style="width:5.20906in;height:3.38589in" />

<img src=".//media/image115.png" style="width:6.5in;height:3.97778in" />

The same steps will be used to create template packages for Core’s
Flight package and its Arrival and FlightData sub-packages. When
finished, Package Browser should appear as follows.

<img src=".//media/image116.png" style="width:3.70885in;height:5.04237in" />

And the directory structure for the Application should be organized as
shown below.

<img src=".//media/image117.png" style="width:2.37533in;height:1.85443in" />

#### Create Template Content

The root mechanism for creating template content is making use of the
“XSDrestriction” stereotype built into Sparx EA. When applied to a
Generalization connector between two classes, this results in a schema
restriction on the simpleType or complexContent definition, depending on
the nature of the classes, of the derived class in the physical model.
Put simply, these XSD restrictions allow you to create derived classes
with fewer fields and/or more restricted content than the classes they
are derived from.

We will illustrate in more detail how these restrictions are applied by
looking first at how to constructe the ArrivalAlert template. When
finished, this template should provide the following fields:

-   1 ExampleMessage with:

    -   1 sender

    -   1..99 recipients

    -   1 timestamp

    -   1 type (set to ARRIVAL)

    -   1 flight with:

        -   1 arrival with:

            -   1 actualTimeOfArrival

            -   1 arrivalAerodrome

        -   1 gufi

        -   1 flightIdentification with:

            -   1 aircraftIdentification

        -   0..1 flightType

When constructing a template, we found it easiest to start at the leaf
(outermost) fields and work backwards to the root (innermost) fields.

##### Create a Restricted Class (Complex Type)

1.  Double click on your message template’s diagram (or right click it
    and choose “Open”) to get started. In this example, we began with
    the “ExampeAA\_Arrival” diagram.

2.  Locate the class you wish to restrict in Project Browser and then
    left click and drag the class into your diagram (in this example,
    Fixm -&gt; Core -&gt; Flight -&gt; Arrival -&gt;
    &lt;&lt;XSDcomplexType&gt;&gt;Arrival). Select “Link” under the
    *Drop As* dropdown box and then click Okay.

<img src=".//media/image118.png" style="width:3.75052in;height:2.02112in" />

1.  Create a new class of the same type as the class you wish to
    restrict. In this example, that would be a complexType class,
    created as outlined in [Create a ComplexType
    Class](#create-a-complextype-class). The *Name* and *Annotation*
    should be the same as the class you are restricting except the
    *Name* should begin with your template’s prefix.

<img src=".//media/image119.png" style="width:5.09446in;height:3.83387in" />

1.  Click on your new restricted class in the diagram. You will see an
    upward arrow icon
    \[<img src=".//media/image79.png" style="width:0.10156in;height:0.15625in" />\]
    appear near the upper right hand corner of the class. Click on this
    arrow and drag it over the class you are restricting. Then release
    the mouse button and choose “Generalization” from the list of
    options that pops up.

<img src=".//media/image120.png" style="width:4.89652in;height:3.36505in" />

<img src=".//media/image121.png" style="width:3.3338in;height:3.30254in" />

1.  Double click (or right click and choose “Properties…”) on the
    generalization connector to open the Generalization Properties
    dialogue box.

2.  Click on the far right side of the *Stereotype* field under the
    *Connector Properties* table of the *Main* tab on the right hand
    side of the dialogue box. This should open a Stereotype dialogue
    box. Check the box next to “XSDrestriction” and click Okay.

<img src=".//media/image122.png" style="width:6.5in;height:4.30278in" />

1.  Then click Okay in the Generalization Properties dialogue box to
    apply the stereotype.

<img src=".//media/image123.png" style="width:3.31296in;height:3.30254in" />

Any class attributes and associations that resolve to XML elements in
the physical model that are not included in a restricted class will be
removed[27]. At this point, our example restricted class is completely
empty. The next step is to add back in the attributes and associations
you wish to retain.

##### Set Up Restricted Class Attributes (Complex Type)

We will begin with class attributes. If desired, attributes can be added
by following the steps listed in [Add an Attribute to a
Class](#add-an-attribute-to-a-class), being sure to replicate the values
used by the attributes in the class you are restricting. However, the
steps listed below can be used as a shortcut that should make adding the
attributes both easier and less error prone.

1.  Once again, locate the class you wish to restrict in Project Browser
    (in this example, Fixm -&gt; Core -&gt; Flight -&gt; Arrival -&gt;
    &lt;&lt;XSDcomplexType&gt;&gt;Arrival). Click on the arrow
    \[<img src=".//media/image124.png" style="width:0.12502in;height:0.16669in" />\]
    to the left of the class to display its associated attributes.

<img src=".//media/image125.png" style="width:3.94847in;height:5.06321in" />

1.  Control-left-click on each attribute you wish to retain in your
    restriction. In this example, “actualTimeOfArrival” and
    “arrivalAerodrome”.

<img src=".//media/image126.png" style="width:3.93805in;height:5.03195in" />

1.  Now drag the selected attributes onto your restricted class in the
    diagram. In the example, the attributes will be dragged onto the
    ExampleAA\_Arrival class in the ExampleAA\_Arrival diagram. This
    will create exact replicas of the attributes within your restricted
    class.

<img src=".//media/image127.png" style="width:3.32338in;height:3.17753in" />

Next, adjust the *Multiplicity* of your attributes to suit your
template’s needs.

1.  Right click on the restricted class in the diagram and choose
    “Features and Properties” and then “Attributes…”. Select the
    attribute you wish to adjust and then click on *Multiplicity* in the
    *Attribute* section to change its value. In this example, both
    “actualTimeOfArrival” and “arrivalAerodrome” should be given an
    upper and lower bound of “1”.

<img src=".//media/image128.png" style="width:6.5in;height:3.89028in" />

Most attributes in FIXM Core are marked as nillable. This is done via
adding a tag to the field with *Tag* set to “nillable” and *Value* set
to “true”.

<img src=".//media/image129.png" style="width:6.5in;height:3.87847in" />

1.  If you do not wish attributes in your template to be nillable,
    navigate to the *Tagged Values* tab, and then erase the nillable tag
    by clicking on it and then clicking the fifth icon from the left
    \[<img src=".//media/image130.png" style="width:0.15417in;height:0.14646in" />\].
    In this example, the nillable tags should be erased from all
    attributes with a multiplicity lower bound of “1” or higher.

<img src=".//media/image131.png" style="width:6.5in;height:3.875in" />

1.  Click Close when finished. You should see the new multiplicities
    reflected in the restricted class diagram.

<img src=".//media/image132.png" style="width:3.32338in;height:3.16711in" />

##### Set Up Restricted Class Associations

Next, we will focus on setting up associations. Like attributes, any
associations that resolve to XML elements not added back to your
restricted class will be removed. For example, the “reclearanceInFlight”
association attached to Core’s Arrival class (shown below) was removed
from ExampleAA\_Arrival because the association was never recreated.

<img src=".//media/image133.png" style="width:4.1985in;height:3.08376in" />

To find an example of retained associations, let us move on to the
restricted FlightData package.

Following the steps outlined so far in [Create Template
Content](#create-template-content), create restricted versions of the
“Flight” and “FlightIdentification” classes from Fixm -&gt; Core -&gt;
Flight -&gt; FlightData in the ExampleAA\_FlightData diagram. For our
new “ExampleAA\_Flight” class, the “gufi” attribute should be retained
and made required (*Multiplicity* of 1..1). For
“ExampleAA\_FlightIdentification”, the “aircraftIdentification”
attribute should be retained and made required. Below are examples of
how Project Brower and the diagram will appear after this is done.

<img src=".//media/image134.png" style="width:5.13613in;height:5.04237in" />

<img src=".//media/image135.png" style="width:6.5in;height:2.62847in" />

Much like “reclearanceInFlight” from the Arrival package, all of the
associations attached to the Flight class in Core have been implicitly
restricted away for ExampleAA\_Flight. To retain them, they must be
added back in by hand.

In this example, the first association we will add back in is
“flightType”.

1.  If the class you wish to add an association to is not already
    present in the diagram, locate it in Project Brower and drag it into
    the diagram. In this example, “Fixm -&gt; Core -&gt; Flight -&gt;
    FlightData -&gt; TypeOfFlight” should be added to the
    ExampleAA\_FlightData diagram.

<img src=".//media/image136.png" style="width:6.5in;height:2.43056in" />

1.  Use the steps detailed in [Add an Association Between
    Classes](#add-an-association-between-classes) to create the
    association desired for your restricted class. Like with class
    attributes, you will want to reuse all of the same values as the
    original association with the possible exception of multiplicity and
    removing the nillable tag. You will also likely need to modify the
    “position” tag to make sure your elements are ordered correctly in
    the physical model. In this example, use all of the same values used
    in the original “flightType” association except position (which will
    end up being set to “3” in the final version of this template).

<img src=".//media/image137.png" style="width:6.5in;height:4.10903in" />

<img src=".//media/image138.png" style="width:6.5in;height:2.45208in" />

Sparx EA automatically displays any associations between classes you add
to a diagram. Above you will notice this for the existing associations
“flightType” and “flightIdentification”. To improve the readability of
your diagrams, it is recommended you hide (not delete[28]) these
associations.

1.  Right click on the any existing associations you do not want to show
    in your diagram and choose “Visibility” and then “Hide Connector”.
    In this example, the pre-existing “flightType” and
    “flightIdentification” associations were hidden.

<img src=".//media/image139.png" style="width:6.5in;height:5.72708in" />

<img src=".//media/image140.png" style="width:6.5in;height:2.46319in" />

##### Use a Restricted Class to Enforce the Use of Another Restricted Class

The next association that needs to be created for the example will be
used to add back in the “flightIdentification” field to the restricted
ExampleAA\_Flight class. However, we only want to allow the use of the
restricted ExampleAA\_FlightIdentification class, not the original
unrestricted FlightIdentification class from Core.

While doing so is mechanically no different than the steps outlined
above in [Set Up Restricted Class
Associations](#set-up-restricted-class-associations), this chaining
together of restricted classes (ultimately all the way back to the root
class of your Application) is the means by which templates are formed
and enforced[29].

Below are a series of screenshots capturing key steps taken along the
way to completing the restricted FlightData package. Each of these steps
involves enforcing the use of a restricted class.

<img src=".//media/image141.png" style="width:6.5in;height:4.11875in" />

<img src=".//media/image142.png" style="width:6.5in;height:2.44931in" />

<img src=".//media/image143.png" style="width:4.49021in;height:5.03195in" />

<img src=".//media/image144.png" style="width:3.80261in;height:2.05237in" />

<img src=".//media/image145.png" style="width:6.5in;height:3.55833in" />

<img src=".//media/image146.png" style="width:6.5in;height:4.07847in" />

<img src=".//media/image147.png" style="width:6.5in;height:3.57778in" />

With the FlightData package complete, the only package left to finish
for the ArrivalAlert template is ExampleMessage.

##### Create a Restricted Class (Enumeration)

When creating the final ArrivalAlert restricted package
(ExampleMessage), we run into a new use of XSD restriction: limiting an
enumeration to only allow a specific value.

1.  Similar to [Create a Restricted Class (Complex
    Type)](#create-a-restricted-class-complex-type), begin by dragging
    the enumeration you wish to restrict into your diagram. In this
    example, “AlertType” from Fixm -&gt; Applications -&gt;
    ExampleMessage should be added to the “ExampleAA\_ExampleMessage”
    diagram.

2.  Next, add a new enumeration to the diagram as outlined in [Create an
    Enumeration Class](#create-an-enumeration-class). However, the
    *Name* field should begin with your message template’s prefix (in
    this example, “MessageAA\_”) followed by the same name as the
    enumeration you are restricting, the *Annotation* should be the same
    as the enumeration you are restricting, and the *Values* should only
    include the value you wish to enforce in this template (in this
    example, “ARRIVAL”).

<img src=".//media/image148.png" style="width:5.15697in;height:3.91721in" />

1.  Next click on the “…” icon to the right of the *Type* field. This
    opens the Select Classifier dialogue box. In the *Browse* tab,
    navigate to and click on the class you would like your restriction
    to be derived from. In this example, Fixm -&gt; Applications -&gt;
    ExampleMessage -&gt; AlertType. Click OK.

<img src=".//media/image149.png" style="width:6.44882in;height:4.83401in" />

1.  You will see the selected class show up in the *Type* field. Click
    OK to create the enumeration.

<img src=".//media/image150.png" style="width:5.17781in;height:3.9068in" />

<img src=".//media/image151.png" style="width:1.31268in;height:2.19822in" />

1.  Finally, as done in [Create a Restricted Class (Complex
    Type)](#create-a-restricted-class-complex-type), apply the
    XSDrestriction stereotype to your generalization connector to finish
    constructing your restricted enumeration class.

<img src=".//media/image152.png" style="width:1.33352in;height:2.19822in" />

The rest of the restricted ExampleMessage package should be created
using the techniques covered above in [Create Template
Content](#create-template-content). Below are a series of screenshots
capturing key steps taken along the way.

<img src=".//media/image153.png" style="width:3.38589in;height:5.02153in" />

<img src=".//media/image154.png" style="width:3.76094in;height:2.03153in" />

<img src=".//media/image155.png" style="width:5.06321in;height:3.82345in" />

<img src=".//media/image156.png" style="width:3.87554in;height:1.69815in" />

<img src=".//media/image157.png" style="width:4.52146in;height:2.28157in" />

<img src=".//media/image158.png" style="width:3.37547in;height:5.04237in" />

<img src=".//media/image159.png" style="width:4.38603in;height:2.32324in" />

<img src=".//media/image160.png" style="width:6.5in;height:3.89583in" />

<img src=".//media/image161.png" style="width:4.45896in;height:2.34408in" />

<img src=".//media/image162.png" style="width:6.5in;height:4.05486in" />

<img src=".//media/image163.png" style="width:4.40686in;height:2.31282in" />

<img src=".//media/image164.png" style="width:6.5in;height:4.12014in" />

<img src=".//media/image165.png" style="width:4.53188in;height:2.36491in" />

<img src=".//media/image166.png" style="width:5.14655in;height:5.03195in" />

<img src=".//media/image167.png" style="width:3.75052in;height:2.02112in" />

<img src=".//media/image168.png" style="width:6.5in;height:4.10347in" />

<img src=".//media/image169.png" style="width:6.5in;height:2.11597in" />

<img src=".//media/image170.png" style="width:5.43826in;height:2.18781in" />

At this point in the example Application, the ArrivalAlert message
template should be complete and it is time to create the DepartureAlert
template. The intended content of the DepartureAlert template is very
close to the structure and content of ArrivalAlert:

-   1 ExampleMessage with:

    -   1 sender

    -   1..99 recipients

    -   1 timestamp

    -   1 type (set to DEPARTURE)

    -   1 flight with:

        -   1 departure with:

            -   1 actualTimeOfDeparture

            -   1 aerodrome

        -   1 gufi

        -   1 flightIdentification with:

            -   1 aircraftIdentification

        -   0..1 flightType

Only the value of the “type” field and the replacement of “arrival” with
“departure” (and associated sub-fields) differ between the two, making
this a good candidate for copying and pasting template content (see
[Copying and Pasting a Template
Package](#copying-and-pasting-a-template-package) below).

Before employing this technique, the portions of DepartureAlert that are
not a good candidate for copy and paste (specifically the Flight package
and the Departure package) should be created as described in [Create
Template Content](#create-template-content) above. Do so now. Below are
screenshots of showing how Project Browser and the restricted Departure
package diagram should look after these packages have been completed.

<img src=".//media/image171.png" style="width:4.6569in;height:5.04237in" />

<img src=".//media/image172.png" style="width:3.40673in;height:3.12544in" />

### Copying and Pasting a Template Package

Copying and pasting content in EA can be dangerous if proper care is not
taken. It is easy to accidentally create hidden relationships or cause
other unexpected issues. However, it can also be very helpful in terms
of saving effort and avoiding errors that sometimes creep in when
creating content by hand. The restricted FlightData and ExampleMessage
packages from the ArrivalAlert template are good candidates for using
this technique to create corresponding packages under DepartureAlert. In
this example, we will begin with FlightData.

1.  Right click on package you would like to copy in Project Browser and
    choose “Copy / Paste” and then “Copy to Clipboard” and then “Full
    Structure of Duplication”.

<img src=".//media/image173.png" style="width:6.5in;height:5.19375in" />

1.  Next, right click on the package under which you want to paste your
    copied package and choose “Copy / Paste” and then “Paste Package
    from Clipboard”. In this example, that is the “Flight” package under
    “DepartureAlert”.

<img src=".//media/image174.png" style="width:6.5in;height:7.27222in" />

At this point, your copied package should be replicated in the new
location. You will now need to go through it and adjust settings as
needed for this version of the package.

1.  Double click (or right click and choose “Properties…”) on your
    copied package in Project Browser to access and adjust the schema
    properties. In this example, only the *Schema Location* field needs
    to be adjusted. It should be modified to use:
    “.\\schemas\\applications\\examplemessage\\exampletemplates\\departurealert\\flight\\flightdata\\ExampleDA\_FlightData.xsd”[30].
    Click OK to save the new settings.

2.  Again, double click (or right click and choose “Properties…”) on
    your copied package in Project Browser and this time click the UML
    button in the upper right hand corner. In the central text box,
    adjust the schema description as needed. In this example, the text
    should be changed to read “An example Departure Alert message
    template for the FlightData package.”. Click OK to save the change.

<img src=".//media/image175.png" style="width:6.5in;height:3.96181in" />

1.  Right click and choose “Properties…” on your diagram name in Project
    Brower. In this example, that will be “ExampleAA\_FlightData” within
    the DepartureAlert template.

<img src=".//media/image176.png" style="width:6.08418in;height:6.35505in" />

1.  This opens the Class Diagram dialogue box. Change the *Name* field
    to something appropriate for your package. In this example,
    “ExampleDA\_FlightData”.

<img src=".//media/image177.png" style="width:3.72969in;height:0.78136in" />

1.  In Project Browser, delete any unwanted classes from your package by
    right clicking on them and choosing “Delete ‘\[class name\]’”. In
    this example, no classes need to be deleted.

2.  In Project Brower, double click (or right click and choose
    “Properties…”) on each class in your package and update the *Name*
    field as needed. In this example, each *Name* should be modified to
    use a prefix of “ExampleDA\_” rather than “ExampleAA\_”.

<img src=".//media/image178.png" style="width:5.09446in;height:3.82345in" />

<img src=".//media/image179.png" style="width:5.09446in;height:3.84429in" />

1.  Now review your class diagram by double clicking on its name (or
    right click it and choose “Open”).

2.  Note any connectors that are no longer desired. Delete these by
    right clicking on them and choosing “Delete Connector”[31]. In this
    example, the “arrival” connector between ExampleDA\_Flight and
    ExampleAA\_Arrival is no longer desired and should be removed.

<img src=".//media/image180.png" style="width:3.76094in;height:5.96958in" />

> When prompted, select the “Delete the connector from the model” radio
> button and then click OK.
>
> <img src=".//media/image181.png" style="width:2.7608in;height:2.08362in" />
>
> <img src=".//media/image182.png" style="width:6.5in;height:3.5875in" />

1.  Note any orphaned classes left behind when the unwanted connectors
    have been removed. Click on each in turn and press the delete key
    (or right click on them and choose “Delete ‘\[class name\]’”).
    Unlike connectors, this will only remove the class from the diagram,
    not erase it entirely from the model. In this example, the
    ExampleAA\_Arrival class should be deleted from the diagram.

<img src=".//media/image183.png" style="width:5.61537in;height:1.35436in" />

1.  Next, use the techniques outlined in [Create Template
    Content](#create-template-content) to finish adjusting your package
    with any more changes needed. In this example, that involves
    creating a “departure” association between ExampleDA\_Flight and
    ExampleDA\_Departure (defined in the already created restricted
    Departure package under DepartureAlert). Don’t forget to adjust
    position tags as needed to ensure correct ordering of elements in
    the physical model.

<img src=".//media/image184.png" style="width:6.5in;height:3.5625in" />

As a final check when performing any copy and paste in Sparx EA, you
will want to review the relationships of each class you copied to ensure
no undesired connections exist.

1.  In the *Start* ribbon at the top of the screen, select
    “Relationships” from the *Windows* section to open the Relationships
    window.

<img src=".//media/image185.png" style="width:2.09404in;height:0.96889in" />

1.  Click on each class in your package and review the displayed
    relationships for any unexpected connections. In this example, the
    Relationships window will reveal an unwanted connection between
    ExampleDA\_Flight and ExampleAA\_ExampleMessage that resulted from
    the copy and paste!

<img src=".//media/image186.png" style="width:6.5in;height:1.86528in" />

1.  Right click and choose “Delete Connection” for any unwanted
    relationships. Click Yes when asked to confirm the deletion.

<img src=".//media/image187.png" style="width:5.7508in;height:4.43812in" />

<img src=".//media/image188.png" style="width:3.8547in;height:1.81275in" />

The steps outlined above should be repeated for the ExampleMessage
package to complete the DepartureAlert template. Below are screenshots
of how Project Browser and the restricted ExampleMessage package diagram
should appear after this package is completed.

<img src=".//media/image189.png" style="width:5.1153in;height:7.36561in" />

<img src=".//media/image190.png" style="width:6.5in;height:2.16667in" />

The templates created for this example were relatively simple and
contained very few fields when compared to FIXM’s entire structure.
However, the techniques outlined in [Create
Templates](#create-templates) were the same ones employed to create the
much larger set of FF-ICE Message templates and should provide the
framework needed to create larger, more complicated templates as needed.

### Create the Includes Package 

The final step in creating Templates is to add an “Includes” package and
appropriate sub-packages. FIXM makes use of “package-wide include files”
to increase its usability with a number of XML tools. The packages
contained under the Includes package facilitate this and will be
modified by the post-processing script to contain the needed content
(see [Set Up and Use Package-Wide Include
Files](#set-up-and-use-package-wide-include-files) below for more
details).

1.  Right click on your overall templates container (in this example,
    the “ExampleTemplates” package) and choose “Add a Package…”.

2.  In the New Package dialogue box, change the *Name* field to
    “Includes”.

3.  Select the “Package Only” radio button and click OK.

<img src=".//media/image191.png" style="width:3.69843in;height:2.97958in" />

1.  For each namespace your templates both import and restrict (in this
    example, only “http://www.fixm.aero/flight/4.2”), create one
    sub-package under Includes. Like Includes itself, these sub-packages
    will be “Package Only”. Choose a *Name* appropriate to both your
    templates and the schemas they will import. In this example, one
    sub-package will be created and it should be named “ExampleFlight”.

<img src=".//media/image192.png" style="width:3.71927in;height:2.94833in" />

1.  Follow the steps detailed in [Apply Schema
    Stereotype](#apply-schema-stereotype), [Set Up Schema
    Properties](#set-up-schema-properties), and [Add Schema Description
    and Tags](#add-schema-description-and-tags) to configure this
    package. The *Target Namespace* and *Prefix* fields should match
    those of the schemas you will be importing, as should the “version”
    tag. The *Schema File* field should be set to something appropriate
    for your templates. In this example, use:

<!-- -->

1.  *Target Namespace* set to: “http://www.fixm.aero/flight/4.2”.

2.  *Prefix* set to: “fx”.

3.  *Schema File* set to:
    “.\\schemas\\applications\\examplemessage\\exampletemplates\\ExampleFlight.xsd”.

With the Includes package in place, the example Applications Library is
complete. Below are screenshots showing the final composition of Project
Browser and the schemas directory structure.

<img src=".//media/image193.png" style="width:3.6776in;height:5.33408in" />

<img src=".//media/image194.png" style="width:2.39617in;height:2.60453in" />

