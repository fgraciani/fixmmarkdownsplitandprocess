## Create Application Content

Now it is time to create any content needed for your Application. For
this example, we will create two classes: a complex type for the message
itself and an enumeration for the alert type. The message will have
three attributes added to it and the enumeration will be linked to the
message via an association. We will also add an association to link the
message to Core’s Flight class (the root class for Core). Finally, we
will create a root element for the Application.

1.  Double click on your Application’s diagram (or right click it and
    choose “Open”) to get started.

### Create a ComplexType Class

We will start by creating a class with the XSDcomplexType stereotype for
our message.

1.  In Toolbox, click on “Complex Type” and then click anywhere in the
    diagram section of the screen[22]. This will open up an XSD
    complexType Properties dialogue box.

2.  Add an appropriate *Name* and *Annotation* for your new class.

3.  Then click OK.

<img src=".//media/image68.png" style="width:1.43431in;height:3.464in" /><img src=".//media/image69.png" style="width:4.63542in;height:3.48841in" />

You can now begin to add content to your class.

### Add an Attribute to a Class

For this example, we will add three attributes to this class: sender,
recipient, and timestamp. Because each of these is of a type defined in
Core’s Base package, using attributes is in line with how FIXM is
standardly modeled.

1.  Right click on the class in the diagram and choose “Features and
    Properties” and then “Attributes…”. This opens the Features dialogue
    box. In the Features dialogue box, you can add the attributes needed
    for your Application to your class.

<img src=".//media/image70.png" style="width:4.11265in;height:3.80508in" />

1.  Begin by clicking where it says “New Attribute…” under *Name* and
    filling in your new field’s name. In this example, we will start
    with “sender”.

2.  Then hit the tab key or otherwise click out of the *Name* field.

3.  You should now have a new attribute added to your class with a
    default *Type* of int and *Scope* of Private.

<img src=".//media/image71.png" style="width:6.5in;height:3.4125in" />

1.  Next, click on the *Type* field, select the down arrow on the right
    side, and then click “Select Type…”.

<img src=".//media/image72.png" style="width:2.417in;height:2.11488in" />

1.  This opens the Select Type dialogue box. Navigate to the appropriate
    class in the Base package you want to use, select it, and then click
    OK. In this example, that will be Fixm -&gt; Core -&gt; Base -&gt;
    Organization -&gt; PersonOrOrganization.

<img src=".//media/image73.png" style="width:6.49049in;height:4.85484in" />

1.  Next change the *Scope* field to “Public”.

2.  Adjust the *Multiplicity* in the *Attribute* section as needed (in
    this example, it should be set to 0..1).

3.  Then add a description for the field in the *Notes* section. When
    finished, your Features dialogue box will look something like below.

<img src=".//media/image74.png" style="width:6.5in;height:3.89306in" />

1.  Repeat the steps above to continue adding as many attributes as
    desired. For this example, we will also add:

    1.  A recipient field:

        1.  *Name* set to: “recipient”.

        2.  *Type* set to: “Fixm -&gt; Core -&gt; Base -&gt;
            Organization -&gt; PersonOrOrganization”.

        3.  *Scope* set to: “Public”.

        4.  *Multiplicity* set to: “0..2000”.

    2.  A timestamp field:

        1.  *Name* set to: “timestamp”.

        2.  *Type* set to: “Fixm -&gt; Core -&gt; Base -&gt; Types -&gt;
            Time”.

        3.  *Scope* set to: “Public”.

        4.  *Multiplicity* set to: “0..1”.

2.  When finished, click Close on the Features dialogue box. The class
    diagram should display the name, type, and multiplicity of each
    attribute added to the class.

<img src=".//media/image75.png" style="width:2.39617in;height:0.95847in" />

### Create an Enumeration Class

Next, we will create an enumeration class to represent the type of the
alert.

1.  In Toolbox, click on “Enum” and then click anywhere in the diagram
    section of the screen. This will open up an XSD enumeration
    Properties dialogue box.

2.  Add an appropriate *Name*, comma-delimited set of *Values*, and
    *Annotation* for your new class. For the *Type* field, FIXM
    standardly leaves this blank. When generating schemas, the physical
    model will still derive this enumeration from xs:string but leaving
    the field blank avoids displaying the string inheritance in the
    model diagrams.

3.  Then click OK.

<img src=".//media/image76.png" style="width:5.14655in;height:3.88596in" />

1.  Right click on the enumeration class in the diagram and choose
    “Features and Properties” and then “Attributes…”. This opens the
    Features dialogue box.

<img src=".//media/image77.png" style="width:5.03121in;height:4.17708in" />

1.  In the Features dialogue box, you can add descriptions to each
    enumeration in the *Notes* tab. When finished, click OK.

<img src=".//media/image78.png" style="width:6.5in;height:3.875in" />

### Add an Association Between Classes

When converted to XSD schemas, there is no difference between
representing a field as an attribute of a class versus representing a
field as an association between two classes. However, FIXM standardly
only uses attributes for fields of a type defined in Core’s Base
package. Any other classes you want to use as a field under a class
should be attached to the class via an association.

In this example, we will use an association to create the alert type
field needed for our message because our AlertType enumeration was not
defined under the Base package.

1.  Click on the class you wish to add your field to. You will see an
    upward arrow icon
    \[<img src=".//media/image79.png" style="width:0.10156in;height:0.15625in" />\]
    appear near the upper right hand corner of your class.

<img src=".//media/image80.png" style="width:2.77122in;height:1.11474in" />

1.  Click on this arrow and drag it over the class you wish to use as
    the type of your field. Then release the mouse button and choose
    “Association” from the list of options that pops up.

<img src=".//media/image81.png" style="width:3.08376in;height:3.83387in" />

1.  This will create an association between the two classes.

<img src=".//media/image82.png" style="width:2.40659in;height:2.37533in" />

1.  Double click (or right click and choose “Properties…”) on the
    association to open the Association Properties dialogue box.

2.  Begin by clicking on the far right side of the *Direction* field
    under the *Connector Properties* table of the *Main* tab on the
    right hand side of the dialogue box. This should open a dropdown
    menu. From this menu, choose “Source -&gt; Destination”.

<img src=".//media/image83.png" style="width:6.5in;height:4.10833in" />

1.  Next, select “Role(s)” from the tree of options in the upper left
    hand corner. This brings up a new section of the Association
    Properties dialogue box split between setting up details for the
    source and target sides of your new association.

<img src=".//media/image84.png" style="width:6.5in;height:4.11111in" />

1.  In the text/dropdown box directly under TARGET in the upper right
    hand corner, type in the name you would like to use for the field
    represented by this association (“type” in this example).

2.  In the next text box down, fill in a short description for this
    field.

3.  Finally, choose an appropriate *Multiplicity* for this field (“0..1”
    in this example).

4.  When finished, your Association Properties dialogue box will look
    something like below. Click OK to save these settings.

<img src=".//media/image85.png" style="width:6.5in;height:4.12083in" />

In this example, we will also add an association between ExampleMessage
and the Flight class (the root class of FIXM Core).

1.  To accomplish this, first navigate to the correct package in Project
    Browser (Fixm -&gt; Core -&gt; Flight -&gt; FlightData) and then
    select the “&lt;&lt;XSDcomplexType&gt;&gt;Flight” class.

<img src=".//media/image86.png" style="width:3.36505in;height:5.04237in" />

1.  Now click and drag the Flight class from Project Browser to the
    ExampleMessage diagram. When you release the mouse button, a
    dialogue box will appear asking you how you would like to paste the
    class into the diagram. Select “Link” under the *Drop As* dropdown
    box and then click Okay.

<img src=".//media/image87.png" style="width:3.77136in;height:2.0107in" />

1.  Next, follow the same steps detailed above to create an association
    from the ExampleMessage class to the Flight class. When finished,
    your diagram should look something like below.

<img src=".//media/image88.png" style="width:6.04251in;height:2.68788in" />

The final step in creating associations is to add “position” tags. Sparx
EA will automatically alphabetize class attributes when creating schemas
from the logical model but associations need to be handled explicitly.
Once all associations have been created for a class, follow the steps
below to make sure the fields derived from associations are properly
ordered in the physical model.

1.  In the *Start* ribbon at the top of the screen, select “Tagged
    Values” from the *Windows* section to open the Tagged Value window.
    Having this window open provides a shortcut to accessing tagged
    values and is very useful when adding position tags.

<img src=".//media/image89.png" style="width:2.68788in;height:0.96889in" />

1.  Next, determine the correct ordering for each association
    originating from your class. For this example, the ExampleMessage
    class will have three attributes and two associations. Ordering the
    group of fields as a whole alphabetically gives you: flight,
    recipient, sender, timestamp, type. The position of the field in
    this alphabetical list gives you the value (starting with “1” for
    the first field) needed when adding a position tag. So, for this
    example, “flight” will need a position tag with a value of “1” and
    “type” will need a position tag with a value of “5”[23].

2.  Now, click on each association in turn. When clicked on, you will
    see all the tagged values associated with whatever you click on show
    up in the Tagged Values window. For these associations, this window
    will initially look like the image below.

<img src=".//media/image90.png" style="width:4.17767in;height:4.15683in" />

1.  Click on *Connector Source* and then click on the third icon from
    the left
    \[<img src=".//media/image63.png" style="width:0.19001in;height:0.15347in" />\]
    to add a new tagged value. The *tag* field should be set to
    “position” and the *value* field to the correct numeric value as
    determined above. In this example, the flight association,
    connecting ExampleMessage to Flight, should be given the following
    tag:

> <img src=".//media/image91.png" style="width:3.54167in;height:1.69601in" />
> <img src=".//media/image92.png" style="width:3.53125in;height:3.52247in" />
>
> The type association, connecting ExampleMessage to AlertType, should
> be set up as below:
>
> <img src=".//media/image93.png" style="width:3.52083in;height:1.67141in" />
>
> <img src=".//media/image94.png" style="width:3.48958in;height:3.48958in" />

### Add a Root Element

Each XML document has exactly one single root element. It encloses all
the other elements and is therefore the sole parent element to all the
other elements. Applications create one or more elements that serve as
an entry point to the model and can therefore be used as root elements.
For this example, we will create a single such entry point named
“ExampleMessage”.

1.  In Toolbox, click on “Element” and then click anywhere in the
    diagram section of the screen. This will open up an XSD element
    Properties dialogue box.

2.  Add an appropriate *Name* (in this example, “ExampleMessage”) and
    *Annotation* (in this example, “The ExampleMessage element is an
    entry point to the Example Message application.”) for your
    Application.

<img src=".//media/image95.png" style="width:5.27157in;height:4.07349in" />

1.  Next click on the “…” icon to the right of the *Type* field. This
    opens the Select Classifier dialogue box. In the *Browse* tab,
    navigate to and click on the class you would like to use as the
    entry point for your Application. In this example, Fixm -&gt;
    Applications -&gt; ExampleMessage -&gt; MessageType. Click OK.

<img src=".//media/image96.png" style="width:6.45923in;height:4.84443in" />

1.  The *Type* field should now be updated to your selection. Click OK
    to create your root element. Note the generalization link formed
    between the element and the class it is based on.

<img src=".//media/image97.png" style="width:6.5in;height:2.17222in" />

Repeat the steps above to add elements for each intended entry point
into your Application.

1.  Continue adding as many classes, attributes, associations, and
    elements as needed for your particular Application. When finished,
    right click on the name at the top of the diagram and click “Save
    Changes to ‘\[diagram name\]’”.

<img src=".//media/image98.png" style="width:4.18808in;height:2.22948in" />

The Application presented here is simple but keep in mind that the steps
detailed in this guide can be used to create as many packages and as
much content as needed to capture all the structure, headers, and
metadata needed for your particular exchange.

