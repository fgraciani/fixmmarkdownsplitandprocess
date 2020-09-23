This document provides guidance and clarifications for the
implementation of FIXM. It includes general guidance for the
implementation of FIXM (high-level considerations about the usage of
FIXM, general encoding rules…) and more specific FIXM guidance and
examples in support of FF-ICE/R1 and of the transition to FF-ICE/R1.

This Guidance Document, which is managed by the FIXM CCB, is released as
a recommended practice for FIXM. It is therefore non-normative.
Requirements described in it shall be considered mandatory only for
those aiming to comply with this guidance.

This document aims to build a "community knowledge" about the
implementation of FIXM. It will therefore evolve over time in order to
capture more alternatives, options and recommendations related to the
use of FIXM. Suggested additions, changes and comments on this document
are welcome and encouraged. These suggestions should be sent to the FIXM
CCB (<FIXM.CCB@eurocontrol.int>) or posted to the FIXM Work Area.

The present version of the document provides guidance for the
implementation of **FIXM v4.2.0**.

***Copyright (c) 2020, Members of the FIXM CCB***

***===========================================***

***All rights reserved.***

***Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:***

***\* Redistributions of source code must retain the above copyright
notice, this list of conditions and the disclaimer.***

***\* Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the disclaimer in the documentation
and/or other materials provided with the distribution.***

***\* Neither the names of the FIXM CCB members nor the names of their
contributors may be used to endorse or promote products derived from
this specification without specific prior written permission.***

***  
DISCLAIMER***

***THIS SPECIFICATION IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.***

***==========================================  
Editorial note: this license is an instance of the BSD license template
as provided by the Open Source Initiative:  
**<http://www.opensource.org/licenses/bsd-license.php>*

***The authoritative reference for FIXM is**
[www.FIXM.aero](http://www.FIXM.aero)**.***

***Details on the FIXM CCB and a list of its members is available on
request from fixm.secretariat@eurocontrol.int.***

**Document history**

<table>
<tbody>
<tr class="odd">
<td><h2 id="this-section-requires-an-update.-it-has-not-been-processed-in-the-preparation-of-this-baseline-version.-please-do-not-review-the-contents." class="Appendix---Heading-2">This section requires an update. It has not been processed in the preparation of this baseline version. Please do not review the contents.</h2></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Version</strong></th>
<th><strong>Date</strong></th>
<th><strong>Description of Changes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.0</td>
<td>31-Oct-2016</td>
<td>First version of the FIXM implementation released on www.FIXM.aero as a fragmented set of documents covering (draft) FF-ICE 1 Realization Through FIXM-Based Services, (endorsed) ATS Message Content to FIXM Logical Model Map, v4 and (draft) XML Examples.<br />
Applicable FIXM core version: 4.0.0</td>
</tr>
<tr class="even">
<td>2.0</td>
<td>30-Mar-2018</td>
<td>New version of the FIXM implementation as an integrated, more consistent package.<br />
Applicable FIXM core version: 4.1.0</td>
</tr>
<tr class="odd">
<td>(This document)</td>
<td>TBD</td>
<td>Applicable FIXM core version: 4.2.0</td>
</tr>
</tbody>
</table>

**Document status**

TODO

**  
**

**TABLE OF CONTENT**

[1. Introduction 8](#introduction)

[1.1. Purpose and content 8](#purpose-and-content)

[1.2. Applicable FIXM version 8](#_Toc48643867)

[1.3. Document terms 9](#document-terms)

[1.4. How to improve this document 10](#how-to-improve-this-document)

[1.5. Acronyms and Definitions 11](#acronyms-and-definitions)

[1.6. References 12](#references)

[2. General Guidance on FIXM implementation
14](#general-guidance-on-fixm-implementation)

[2.1. Target audience 14](#target-audience)

[2.2. Understanding FIXM Core, the Application Libraries and the
Extensions
14](#understanding-fixm-core-the-application-libraries-and-the-extensions)

[2.3. Tested Development Environments
25](#tested-development-environments)

[2.4. General encoding rules 25](#general-encoding-rules)

[2.5. Other Topics 53](#other-topics)

[3. Using FIXM in Support of FF-ICE 55](#_Toc48643878)

[3.1. Target audience 55](#target-audience-1)

[3.2. The FF-ICE Application Library for FIXM
55](#the-ff-ice-application-library-for-fixm)

[3.3. FF-ICE Message Templates 57](#ff-ice-message-templates)

[3.4. FF-ICE/R1 Services Description Example
62](#ff-icer1-services-description-example)

[3.5. XML Samples 68](#xml-samples)

[3.6. Extensions and Restrictions 69](#extensions-and-restrictions)

[3.7. Translating FF-ICE FIXM Messages to ATS Messages
69](#translating-ff-ice-fixm-messages-to-ats-messages)

[4. Using FIXM for other use cases 94](#using-fixm-for-other-use-cases)

[4.1. Using FIXM Core without an Application Library
94](#using-fixm-core-without-an-application-library)

[4.2. Using FIXM Core with an Application Library
95](#using-fixm-core-with-an-application-library)

[4.3. Using FIXM Core with an Extension
98](#using-fixm-core-with-an-extension)

[*5.* FIXM XML Samples 102](#fixm-xml-samples)

[5.1. FIXM XML Structural Overview 102](#fixm-xml-structural-overview)

[5.2. FIXM Samples of Uncorrelated ATS Messages
103](#fixm-samples-of-uncorrelated-ats-messages)

[5.3. FIXM Samples of ATS Messages for a Full Flight Life-Cycle
104](#fixm-samples-of-ats-messages-for-a-full-flight-life-cycle)

[5.4. FIXM Samples of 4DT Data 108](#fixm-samples-of-4dt-data)

[APPENDIX A. How to create an Application Library
110](#how-to-create-an-application-library)

[Initial Download and Setup 110](#initial-download-and-setup)

[Create an Application Package 111](#create-an-application-package)

[Create Application Content 117](#create-application-content)

[Create Templates 134](#create-templates)

[Generate the Application Schemas
189](#generate-the-application-schemas)

[Post-Process the Application Schemas
191](#post-process-the-application-schemas)

[Sample XML 195](#sample-xml)

[APPENDIX B. How to create a FIXM Extension
197](#how-to-create-a-fixm-extension)

[Initial Download and Setup 197](#initial-download-and-setup-1)

[Create a Top-Level Extensions Container
197](#create-a-top-level-extensions-container)

[Create an Extension Root Package
199](#create-an-extension-root-package)

[Create Extension Content 205](#create-extension-content)

[Generate the Extension Schemas 215](#generate-the-extension-schemas)

[Post-Process the Extension Schemas
217](#post-process-the-extension-schemas)

[Sample XML 219](#sample-xml-1)

[APPENDIX C. How to generate XML Schemas from a FIXM model using Sparx
Enterprise Architect
221](#how-to-generate-xml-schemas-from-a-fixm-model-using-sparx-enterprise-architect)

[Generating Schemas from the Logical Model
221](#generating-schemas-from-the-logical-model)

[Post-processing the FIXM Schemas
224](#post-processing-the-fixm-schemas)

[APPENDIX D. FF-ICE/R1 Services Description Example – Details and Other
Considerations
227](#ff-icer1-services-description-example-details-and-other-considerations)

[Planning Service 227](#planning-service)

[Filing Service 237](#filing-service)

[Technical assumptions 243](#technical-assumptions)

[Message classification and technology selection
246](#message-classification-and-technology-selection)

[APPENDIX E. Use of Schematron 249](#use-of-schematron)

[APPENDIX F. FIXM Development Tool Compatibility
250](#fixm-development-tool-compatibility)

[Introduction 250](#introduction-1)

[Evaluation Environment 250](#evaluation-environment)

[Apache Axis library and the WSDL2Java tool
252](#apache-axis-library-and-the-wsdl2java-tool)

[Evaluation Results 253](#evaluation-results)

[Future Testing 254](#future-testing)

[Platform Support Matrix 255](#platform-support-matrix)

[APPENDIX G. Appendix F. Developing a Basic Web Service Using FIXM
(Server and Client)
256](#appendix-f.-developing-a-basic-web-service-using-fixm-server-and-client)

[1. Generate JAXB-RI-Bound Source Code 256](#_Toc48643928)

[APPENDIX H. ATS Message to FIXM Mapping
258](#ats-message-to-fixm-mapping)

**TABLE OF FIGURES**

[Figure 1: General structure of a message and role of an Application
Library 18](#_Toc48643978)

[Figure 2: Example of Message Data structures from FF-ICE
19](#_Toc48643979)

[Figure 3: XSD Restriction vs XSD Profile 21](#_Toc48643980)

[Figure 4: Example of FIXM extension satisfying the requirement on
extension content 23](#_Toc48643981)

[Figure 5: Example of FIXM extension NOT satisfying the requirement on
extension content 24](#_Toc48643982)

[Figure 6: Differences between Elevation, Altitude, Height and Ellipsoid
height 46](#_Toc48643983)

[Figure 7: Overview of the FF-ICE Message Application Library content
55](#_Toc48643984)

[Figure 8: Example of FF-ICE Message data structures tracing to the
FF-ICE Implementation Guidance Manual, Appendix B 56](#_Toc48643985)

[Figure 9: Overview of the FF-ICE Message Data Structures
57](#_Toc48643986)

[Figure 10: The FF-ICE Flight Cancellation Message Template
60](#_Toc48643987)

[Figure 33: Sample Flight Plan 72](#_Ref262546549)

[Figure 34: Equipment and Capabilities Object Model 73](#_Ref262546619)

[Figure 35: Departure Date/Time Object Model 74](#_Ref277922327)

[Figure 36: Route Changes Object Model 78](#_Ref456948489)

[Figure 37: Route Object Model 79](#_Ref262546937)

[Figure 38: Route to Revised Destination Object Model
80](#_Ref262547023)

[Figure 39: Route Delay Object Model 81](#_Ref262549907)

[Figure 40: Aircraft Type Object Model 82](#_Ref265180403)

[Figure 41: Departure Aerodrome Object Model 83](#_Ref277670899)

[Figure 42: Arrival Aerodrome Object Model 84](#_Ref265076386)

[Figure 43: Destination and Alternate Object Model 85](#_Ref262563475)

[Figure 44: En-Route Alternate Object Model 87](#_Ref265173251)

[Figure 45: AFIL Object Model 88](#_Ref268982502)

[Figure 46: Supplementary Information Object Model 90](#_Ref277670947)

[Figure 13: FF-ICE interaction for REJ or non-concur flight plan
submission 231](#_Toc498700597)

[Figure 14: Preliminary Flight plan submission example with preliminary
flight plan rejected for having failed data acceptability (REJ)
232](#_Toc48644003)

[Figure 15: Preliminary Flight plan submission example with preliminary
flight plan rejected for having failed operational acceptability (NON
CONCUR) 232](#_Toc48644004)

[Figure 16: Preliminary Flight plan submission example with rejected
(REJ or ACK+NON CONCUR) preliminary flight plan 233](#_Toc48644005)

[Figure 17: FF-ICE interaction with accepted (CONCUR) preliminary flight
plan 233](#_Toc48644006)

[Figure 18: Preliminary Flight plan submission example with accepted
(CONCUR) preliminary flight plan 234](#_Ref508197419)

[Figure 19: Preliminary Flight plan submission example with accepted
(ACK and CONCUR) preliminary flight plan 234](#_Ref508197611)

[Figure 20: FF-ICE interaction with preliminary flight plan that
requires negotiation (NEGOTIATE) 235](#_Toc48644009)

[Figure 21: Preliminary Flight plan submission example with preliminary
flight plan that requires negotiation (NEGOTIATE) 235](#_Ref508264559)

[Figure 22: Preliminary Flight plan submission example with preliminary
flight plan that requires negotiation (ACK and NEGOTIATE)
236](#_Toc48644011)

[Figure 23: FF-ICE interaction for invalid flight plan submission (REJ)
238](#_Toc48644012)

[Figure 24: FF-ICE interaction for non-acceptable flight plan submission
238](#_Toc498700589)

[Figure 25: Flight plan filing submission example with filed flight plan
rejected for having failed data acceptability (REJ) 238](#_Toc48644014)

[Figure 26: Flight plan filing submission example with filed flight plan
rejected for having failed operational acceptability (NOT ACCEPTABLE)
239](#_Toc48644015)

[Figure 27: Flight plan filing submission example with rejected (REJ or
ACT+NON ACCEPTABLE) filed flight plan 239](#_Ref508205480)

[Figure 28: FF-ICE interaction with accepted flight plan
240](#_Toc498700591)

[Figure 29: Flight plan filing example with accepted flight plan
240](#_Toc498700592)

[Figure 30: Flight plan filing submission example with accepted (ACK and
ACCEPTABLE) filed flight plan 240](#_Toc48644019)

[Figure 31: FF-ICE interaction for manually treated flight plan
241](#_Toc498700593)

[Figure 32: Flight plan filing example with manually treated flight plan
241](#_Toc498700594)

[Figure 11: Synchronous and asynchronous communication between eAU and
eASP 243](#_Ref508186374)

[Figure 12: SubscriptionCreationRequest to setup the AMQP end-point
244](#_Toc48644023)

**Tables**

[Table 1: Correspondences between FF-ICE Message templates and their
ICAO Doc 9965 Volume II description 57](#_Toc48644024)

[Table 2: Example of the FF-ICE Flight Cancellation Message
58](#_Toc48644025)

[Table 3: Messages Types Supporting Field 15 75](#_Ref285513293)

[Table 4: Route Changes 77](#_Ref457456350)

[Table 5: Level/Altitude Mapping 91](#_Ref262563709)

[Table 6: Speed Mapping 92](#_Ref262563928)

[Table 7: PAN AIDC ICD Frequency 93](#_Ref456782567)

[Table 8: Column Definitions 258](#_Toc48644031)

[Table 9: Example 259](#_Toc48644032)

[Table 10: Constraint Notation 259](#_Toc48644033)


<table>
<tbody>
<tr class="odd">
<td><h2 id="this-section-requires-an-update.-it-has-not-been-processed-in-the-preparation-of-this-baseline-version." class="Appendix---Heading-2">This section requires an update. It has not been processed in the preparation of this baseline version.</h2></td>
</tr>
</tbody>
</table>

