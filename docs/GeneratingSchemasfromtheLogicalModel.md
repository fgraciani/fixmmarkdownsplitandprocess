## Generating Schemas from the Logical Model

The FIXM models are heavily annotated with stereotypes that allow Sparx
Enterprise Architect (EA) to convert the logical model into XML schema
files. This section describes how to invoke XSD generation in Sparx
EA[36].

1.  Open the .eap file that contains the Logical Model you would like to
    build.

2.  Select the component of the model you would like to build in Project
    Browser[37]. For this example, we will be building FIXM Core (model
    available at
    <https://fixm.aero/releases/FIXM-4.2.0/FIXM_Core_v4.2.0.eap>).

3.  Right click on the chosen component (in this example, “Core”) and
    select “Code Engineering” and then “Generate XML Schema…”.

<img src=".//media/image230.png" style="width:5.27126in;height:4.95588in" />

1.  This brings up the Generate XML Schema dialogue box. There are a
    number of configuration options available in this dialogue box that
    should be set as follows:

    1.  *Encoding*: Set to Unicode (UTF-8)

    2.  *XSD Style*: No options checked.

    3.  *Referenced Package Options*: No options except “Use
        relative-path to reference XSDs” checked.

    4.  *Child Package Options*: “Generate XSD for Child packages”
        checked and “Include &lt;XSDschema&gt; packages” radio button
        selected. Also, all packages you want to build (typically all
        packages listed) checked.

> When finished, your dialogue box should look similar to below.
>
> <img src=".//media/image231.png" style="width:4.9262in;height:6.73958in" />

As you can see from the list of schema locations under the *Filename*
heading, FIXM is natively set up to generate its schema files into a
directory named “schemas” that is located in the same directory as the
.eap file itself. Sparx EA will <u>not</u> automatically create any of
the directories for the path to the files specified in the *Filename*
fields. **They must be created outside of Sparx EA before generating the
schemas.** The paths shown in the *Filename* fields should give you
guidance as to the required directory structure.

1.  Ensure proper directory structure is in place to hold the generated
    schema files.

For this example, the following directory structure must be placed in
the same directory as the .eap file before attempting to generate the
schemas.

> <img src=".//media/image232.png" style="width:2.26073in;height:2.69829in" />

This structure could be created by hand or, to save time, you could copy
the “schemas” directory from an appropriate FIXM release, editing it as
needed if you are building a logical model with custom content.

One final note on this topic: at times EA does not appear to recognize
directories created during an open session. As such, it might be best to
close and then reopen the logical model after the appropriate directory
structure has been created to ensure Sparx EA will have access to it.

1.  With the configuration options set and the schema directories in
    place, click the Generate button to produce the physical model.

> <img src=".//media/image233.png" style="width:5.27157in;height:2.58369in" />

The Progress section of the dialogue box will show each package being
built and will eventually display “Schema Generation Complete” when
finished. There should be no error or warning messages displayed during
this process.

