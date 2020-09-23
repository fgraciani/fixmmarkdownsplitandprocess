## FIXM Samples of ATS Messages for a Full Flight Life-Cycle 

To further expand the sample data, a complete life-cycle set of messages
was constructed for a single flight (DAL18). This approach allowed the
use of most of the ATS message types in a realistic scenario. This data
contained message header input and additional subfields in ATS message
field 3, *message number* and *reference data* (see Field Type 3,
Appendix 3, ICAO Doc 4444), not seen in the earlier samples. These
fields indicate which ATS computers generated and/or exchanged the
messages, and point back to the relevant message when providing response
or follow-up. The field mesg:referenceMessage contains the message uuid
of its associated message, both of which are in the Messaging part of
the FIXM XML.

The scenario which the DAL18 messages illustrate is as follows:

-   DAL18 is a transatlantic flight flying from Detroit (DTW), Michigan
    to London Heathrow (EGGL).

-   The flight departs from Cleveland Center (KZOB), flies through
    Canadian airspace (CZYZ, …), through oceanic airspace (CZQX, EGGX)
    and arrives at the London Air Traffic Control Center (EGTT).

-   The input messages are in ICAO ATS format. They include both
    messages between the airline and ATS facilities, and between ATS
    facilities.

-   The messages contain meta-data comprised of AFTN send and receiving
    addresses along with the day and time of the message. To eliminate
    redundancy, only one or two of each type of message is shown.

*Note: The first two lines of each message (starting with “FF”) are
header data indicating message time and senders and recipients of the
message. The body of the ATS message is contained within parentheses.*

An explanation of the message sequence follows (each message below
corresponds to a sample FIXM message):

1.  The operator, Delta Airlines, files the <u>initial flight plan</u>
    message <u>(FPL)</u> to KZOB, which is the departure center. This
    message is incorrect with regard to the flight’s route information
    (a “0” was placed in the unit of measure field for the airspeed in
    the Route Designator Field Type 15). A rejection message (rather
    than an ACK) is generated in response to this message because of the
    incorrect unit of measure. The rejection message is not shown.
    *Note: This is not something expected to happen in reality, but is
    an artificial case created to illustrate a logical reject of a
    message.*

> **FF KZOBZZQA  
> 240040 KATLDALQ  
> (FPL-DAL18-IS  
> -B763/H-SDE2E3FGHIJ3J5M1RWXYZ/LB1D1  
> -KDTW0314  
> -0454F330 DCT PISTN DCT KARIT DCT YXI DCT YMW DCT YLQ DCT  
> BAREE N505A RIKAL/M078F350 NATR SUNOT/M078F350 NATR  
> KESIX/M078F350 DCT REVNU/N0441F370 DCT LIFFY UL975 WAL UY53  
> NUGRA DCT  
> -EGLL0715 EGKK  
> -PBN/A1B1C1D1L1O1S1T1 DOF/170324 NAV/RNVD1E2A1 REG/N172DN  
> EET/CZYZ0018 CZUL0051 CZQX0240 EGGX0438 EISN0606 EGTT0631  
> SEL/EQAC CODE/A120F3 RMK/TCAS AGCS EQUIPPED NRP USA)**

1.  Delta Airlines re-files the <u>corrected flight plan</u> message to
    KZOB. The previously incorrect unit of measure field has been
    entered properly.

  
**FF KZOBZZQA  
240049 KATLDALQ**

**(FPL-DAL18-IS  
-B763/H-SDE2E3FGHIJ3J5M1RWXYZ/LB1D1  
-KDTW0314  
-N0454F330 DCT PISTN DCT KARIT DCT YXI DCT YMW DCT YLQ DCT  
BAREE N505A RIKAL/M078F350 NATR SUNOT/M078F350 NATR  
KESIX/M078F350 DCT REVNU/N0441F370 DCT LIFFY UL975 WAL UY53  
NUGRA DCT  
-EGLL0715 EGKK  
-PBN/A1B1C1D1L1O1S1T1 DOF/170324 NAV/RNVD1E2A1 REG/N172DN  
EET/CZYZ0018 CZUL0051 CZQX0240 EGGX0438 EISN0606 EGTT0631  
SEL/EQAC CODE/A120F3 RMK/TCAS AGCS EQUIPPED NRP USA)**

1.  Approximately 90 minutes prior to departure, Delta Airlines notifies
    Cleveland Center (KZOB) of a <u>pre-departure delay</u> (DLA) of
    some 40 minutes due to awaiting passengers from a connecting flight.

**FF KZOBZZQA  
240145 KATLDALQ**

(**DLA-DAL18-KDTW0354-EGLL-0)**

1.  69 minutes prior to the expected departure time, the <u>flight
    plan</u> is transmitted to CZYZ Center.

**FF CZYZZRIP  
240245 KZCCZQZX**  
**(FPLKZOB/CZYZ078-DAL18/A5773-IS**

**-B763/H-SDE2E3FGHIJ3J5M1RWXYZ/LB1D1**

**-KDTW0354**

**-N0454F330 DCT PISTN DCT KARIT DCT YXI DCT YMW DCT YLQ DCT BAREE N505A
RIKAL/M078F350 NATR SUNOT/M078F350 NATR KESIX/M078F350 DCT
REVNU/N0441F370 DCT LIFFY UL975 WAL UY53 NUGRA DCT**

**-EGLL0715 EGKK-PBN/A1B1C1D1L1O1S1T1 DOF/170324 NAV/RNVD1A1E2
REG/N172DN EET/CZYZ0018 CZUL0051 CZQX0240 EGGX0438 EISN0606 EGTT0631
SEL/EQAC CODE/A120F3 RMK/TCAS AGCS EQUIPPED NRP USA)  
**

1.  CZYZ immediately responds with a <u>logical acknowledgment message
    (LAM)</u> from the ATS system.

**FF KZCCZQZX**

**240245 CZYZZRIP**  
**(LAMCZYZ/KZOB106KZOB/CZYZ078)**

1.  When the flight departs, 17 minutes after the revised off block
    time, KZOB sends <u>departure message</u> to CZYZ.

**FF CZYZZRIP  
240411 KZCCZQZX**  
**(DEPKZOB/CZYZ080KZOB/CZYZ078-DAL18/A5773-KDTW0411-EGLL0715
EGKK-DOF/170324)**

1.  CZYZ immediately responds with a <u>logical acknowledgement
    message</u> from the ATS system.

> **FF KZCCZQZX  
> 240411 CZYZZRIP**  
> **(LAMCZYZ/KZOB107KZOB/CZYZ080)**

1.  When a flight plan is established, an <u>estimate message (EST)</u>
    is sent by KZOB to CZYZ notifying it of the expected transition for
    the flight.

> **FF CZYZZRIP  
> 240412 KZCCZQZX**  
> **(ESTKZOB/CZYZ156KZOB/CZYZ078-DAL18/A5773-KDTW-PISTN/0422F330-EGLL0715)**

1.  CZYZ immediately responds with a <u>logical acknowledgement
    message</u> to the EST message.

**F KZCCZQZX  
240412 CZYZZRIP**

**(LAMCZYZ/KZOB184KZOB/CZYZ156)**

1.  A change or <u>modification message (CHG)</u> is shown augmenting
    the time at the fix position for the coordination handling between
    KZOB and CZYZ Centers.

> **FF CZYZZRIP  
> 240413 KZCCZQZX**  
> **(CHGKZOB/CZYZ165KZOB/CZYZ078-DAL18/A5773-KDTW0411-EGLL-14/PISTN/0427F330)**

1.  CZYZ immediately responds with a <u>logical acknowledgement
    message</u> to the CHG message.

**FF KZCCZQZX  
240413 CZYZZRIP**

**(LAMCZYZ/KZOB193KZOB/CZYZ165)**

1.  The <u>coordination message (CDN)</u> between the KZOB and CZYZ ATS
    computer systems indicate that a handoff is accomplished at the
    boundary fix PISTN at an agreed upon time and flight level.

> **FF CZYZZRIP  
> 240415 KZCCZQZX**  
> **(CDNKZOB/CZYZ179CZYZ/KZOB078-DAL18/A5773-KDTW0411-EGLL-14/PISTN/0427F230F233A)**

1.  CZYZ immediately responds with a <u>logical acknowledgement
    message</u> to the coordination handling.

**FF KZCCZQZX  
240416 CZYZZRIP**

**(LAMCZYZ/KZOB181KZOB/CZYZ179)**

1.  An <u>acceptance message (ACP)</u> is then transmitted by CZYZ
    Center to ZOB for the coordination handling by Toronto Center.

> **FF CZYZZRIP  
> 240415 KZCCZQZX**  
> **(ACPCZYZ/KZOB180KZOB/CZYZ078-DAL18/A5773-KDTW0411-EGLL)**

1.  CZYZ immediately responds with a <u>logical acknowledgement
    message</u> to the coordination handling.

**FF KZCCZQZX  
240416 CZYZZRIP**

**(LAMCZYZ/KZOB182KZOB/CZYZ180)**

1.  Prior to the coordination exchange with the United Kingdom an
    <u>amended current flight plan (CPL)</u> is transmitted from CZQZ
    (Gander Operations Center) to EGGX (Shanwick Operations Center).

**FF EGGXZDZX  
240605 KZCCZQZX  
(CPLCZQZ/EGGX094-DAL18/A5773-IS-B763/H-SDE2E3FGHIJ3J5M1RWXYZ/LB1D1-KDTW0411-RAKIL/0641-N0454F330
DCT RIKAL/M078F350 NATR SUNOT/M078F350 NATR KESIX/M078F350 DCT
REVNU/N0441F370 DCT LIFFY UL975 WAL UY53  
NUGRA DCT -EGLL0715 EGKK -PBN/A1B1C1D1L1O1S1T1 NAV/RNVD1E2A1 REG/N172DN
EET/CZQX0240 EGGX0438 EISN0606 EGTT0631 SEL/EQAC CODE/A120F3)**

1.  EGGX immediately responds with a <u>logical acknowledgement
    message</u> to the current flight plan.

> **FF KZCCZQZX  
> 240605 EGGXZDZX**  
> **(LAMCZQZ/EGGX033EGGX/CZQZ094)**

1.  A <u>coordination message (CDN)</u> is transmitted for flight
    control at fix RAKIL between CZQX and EGGX Centers.

**FF EGGXZDZX**

**240616 KZCCZQZX**  
**(CDNCZQZ/EGGX037EGGX/CZQZ094-DAL18/A5773-KDTW-EGLL-14/RAKIL/0641F348F350A)**

1.  EGGX immediately responds with a <u>logical acknowledgement
    message</u> to the coordination message.

> **FF KZCCZQZX  
> 240616 EGGXZDZX**  
> **(LAMEGGX/CZQZ040CZQZ/EGGX037)**

1.  An <u>acceptance message (ACP)</u> is sent from EGGX Center to the
    CZQZ ATS computer for the coordination timing.

**FF KZCCZQZX**

**240617 EGGXZDZX**  
**(ACPEGGX/CZQZ039CZYZ/EGGX094-DAL18/A5773-KDTW0411-EGLL)**

1.  CZYZ immediately responds with a <u>logical acknowledgement
    message</u> to the acceptance.

> **FF EGGXZDZX  
> 240616** **KZCCZQZX**  
> **(LAMCZQZ/EGGX041EGGX/EGGX039)**

1.  The flight arrives per the actual flying time of 07 hours and 15
    minutes and the <u>arrival message (ARR)</u> is sent from EGTT to
    KZOB.

**FF KZOBZZQA  
241127 EGTTZDZX**  
**(ARREGTT/KZOB245KZOB/EGTT094-DAL18/A5773-KDTW0411-EGLL1127)**

1.  KZOB immediately responds with a <u>logical acknowledgement
    message</u> to the arrival message back to EGTT.

**FF EGTTZDZX  
241128 KZOBZZQA**  
**(LAMEGTT/KZOB256KZOB/EGTT245)**

