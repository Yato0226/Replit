from fpdf import FPDF

# --- Partnership Agreement Text ---
# (Removed Markdown like '**' as fpdf2 handles formatting differently)
agreement_text = """
GENERAL PARTNERSHIP AGREEMENT
OF
DRIP-O-MATIC

This General Partnership Agreement (the "Agreement") is made and entered into this ______ day of _______________, 2024 (the "Effective Date"), by and among the following individuals (collectively referred to as the "Partners," and individually as a "Partner"):

1.  Stella Marie B. Abanono
2.  Nathaniel G. Bingco
3.  Samantha Jane S. Darullo
4.  Louize Christopher S. Galang
5.  Yuri B. Gatbunton
6.  Neil Vincent E. Jaen
7.  Myke Jonard S. Sentillas

RECITALS

WHEREAS, the Partners desire to associate themselves as partners in a general partnership for the purpose of engaging in the business described herein; and

WHEREAS, the Partners wish to establish their respective rights, duties, and liabilities relating to the Partnership and its business;

NOW, THEREFORE, in consideration of the mutual covenants contained herein, the Partners agree as follows:

ARTICLE I: FORMATION, NAME, AND PURPOSE

1.1 Formation: The Partners hereby form a general partnership (the "Partnership") pursuant to the laws of the Republic of the Philippines.
1.2 Name: The name of the Partnership shall be Drip-o-matic. The business of the Partnership shall be conducted under this name or such other names as the Partners may unanimously agree upon.
1.3 Purpose: The primary purpose of the Partnership is to design, develop, manufacture, market, and sell the "Drip-o-matic" automatic plant care system and related products and services, including automatic irrigation, soil moisture monitoring, temperature regulation, plant misting, and solar power integration, aiming to provide convenient and efficient plant care solutions. The Partnership may also engage in any other lawful business activities related to its primary purpose as the Partners may unanimously agree.
1.4 Principal Place of Business: The principal place of business of the Partnership shall initially be located at STI Academic Center Altaraza Town Center, Tungkong Mangga, CSJDM, or such other location(s) as the Partners may unanimously determine.

ARTICLE II: TERM

2.1 Duration: The Partnership shall commence on the Effective Date and shall continue until dissolved and terminated in accordance with the provisions of this Agreement or by operation of law.

ARTICLE III: CAPITAL CONTRIBUTIONS

3.1 Initial Contributions: Each Partner shall contribute capital to the Partnership as mutually agreed upon. The description and agreed value of the initial capital contributions (which may include cash, property, services, or expertise) made by each Partner shall be detailed in Exhibit A, attached hereto and incorporated herein by reference.
3.2 Additional Contributions: No Partner shall be required to make additional capital contributions unless unanimously agreed upon in writing by all Partners.
3.3 No Interest: No Partner shall be entitled to receive interest on their capital contributions.
3.4 Capital Accounts: An individual capital account shall be maintained for each Partner, reflecting their contributions, share of profits and losses, and distributions.

ARTICLE IV: PROFITS, LOSSES, AND DISTRIBUTIONS

4.1 Allocation of Profits and Losses: Unless otherwise unanimously agreed in writing, the net profits and losses of the Partnership (after deduction of all expenses, including any salaries approved under Article VI) shall be allocated among the Partners in equal shares (i.e., 1/7th each).
4.2 Distributions: Distributions of cash or other property shall be made to the Partners at such times and in such amounts as the Partners may unanimously determine, typically reviewed on a quarterly basis, provided that such distributions do not impair the ability of the Partnership to meet its obligations. Distributions shall be made in proportion to the Partners' respective shares of profits as defined in Section 4.1.

ARTICLE V: MANAGEMENT AND DUTIES

5.1 Management: All Partners shall have the right to participate in the management and control of the Partnership's business.
5.2 Officer Roles: The Partners agree to designate initial officer roles to manage specific operational areas, subject to the overall authority of the Partnership:
    *   Chief Executive Officer (CEO): Yuri B. Gatbunton
    *   Chief Operating Officer (COO): Neil Vincent E. Jaen
    *   Chief Financial Officer (CFO): Samantha Jane S. Darullo
    *   Chief Marketing Officer (CMO): Stella Marie B. Abanono
    *   Chief Technology Officer (CTO): Louize Christopher S. Galang
    *   Chief Sales Officer (CSO): Myke Jonard S. Sentillas
    *   Chief Human Resources Officer (CHRO): Nathaniel G. Bingco
    The specific duties associated with these roles shall be as generally understood for such positions and as further defined by unanimous agreement of the Partners. These are internal management roles; all Partners remain general partners with associated rights and liabilities.
5.3 Decision Making:
    (a) Ordinary Course Decisions: Decisions arising in the ordinary course of the Partnership's business may be made by the designated officer responsible for that area, subject to review by the Partners.
    (b) Major Decisions: The following decisions shall require the unanimous written consent of all Partners:
        (i) Admitting a new Partner;
        (ii) Amending this Agreement;
        (iii) Selling, leasing, or disposing of all or substantially all of the Partnership's assets;
        (iv) Incurring debt or making expenditures outside the approved budget or above a threshold amount of [Specify Amount, e.g., PHP 50,000];
        (v) Changing the primary purpose or nature of the Partnership's business;
        (vi) Merging or consolidating the Partnership with another entity;
        (vii) Filing for bankruptcy or initiating dissolution;
        (viii) Approving annual budgets and major strategic plans.
5.4 Devotion of Time: Each Partner shall devote such time and attention to the Partnership business as is reasonably necessary for the discharge of their agreed-upon duties and responsibilities.

ARTICLE VI: SALARIES AND COMPENSATION

6.1 Salaries: Initially, no Partner shall receive a fixed salary for services rendered to the Partnership. Partners shall be compensated through their share of profits as provided in Article IV. The Partners may unanimously agree in writing to provide salaries or guaranteed payments to one or more Partners at a future date.
6.2 Expense Reimbursement: Partners shall be reimbursed for reasonable and necessary out-of-pocket expenses incurred directly on behalf of the Partnership business, provided such expenses are properly documented and approved according to procedures established by the Partners.

ARTICLE VII: BOOKS, RECORDS, AND BANKING

7.1 Books and Records: The Partnership shall maintain complete and accurate books and records of its business and financial affairs at its principal place of business, in accordance with generally accepted accounting principles (GAAP). Each Partner shall have the right to inspect and copy these records at reasonable times.
7.2 Fiscal Year: The fiscal year of the Partnership shall end on December 31st.
7.3 Banking: All funds of the Partnership shall be deposited in the Partnership's name in such bank account(s) as selected by the Partners. Withdrawals from such accounts shall be made upon the signature(s) of such Partner(s) as designated by unanimous agreement (initially proposed: CEO and CFO jointly, or as otherwise agreed).

ARTICLE VIII: PARTNER WITHDRAWAL, RETIREMENT, DEATH

8.1 Voluntary Withdrawal: Any Partner may withdraw from the Partnership upon providing at least ninety (90) days' prior written notice to the other Partners.
8.2 Buy-Out Option: Upon the withdrawal, retirement, death, or incapacity of a Partner (the "Departing Partner"), the remaining Partners shall have the option, exercisable within sixty (60) days of the event, to purchase the Departing Partner's interest in the Partnership.
8.3 Valuation: The purchase price for the Departing Partner's interest shall be the value of their capital account as of the date of departure, adjusted for profits/losses up to that date, plus or minus any other adjustments agreed upon by the Departing Partner (or their estate) and the remaining Partners. If an agreement on value cannot be reached, the value shall be determined by an independent appraiser mutually acceptable to both parties.
8.4 Payment Terms: The purchase price shall be paid by the remaining Partners (or the Partnership, if agreed) over a period not to exceed [Specify Period, e.g., twelve (12) months], with terms to be mutually agreed upon.
8.5 Dissolution upon Departure: If the remaining Partners do not exercise the option to purchase the Departing Partner's interest, the Partnership may be dissolved in accordance with Article IX.

ARTICLE IX: DISSOLUTION AND LIQUIDATION

9.1 Events of Dissolution: The Partnership shall be dissolved upon the occurrence of any of the following:
    (a) The unanimous written agreement of all Partners to dissolve;
    (b) The expiration of the term, if specified and not extended;
    (c) The sale or disposition of all or substantially all Partnership assets;
    (d) An event making it unlawful for the business of the Partnership to be carried on;
    (e) Entry of a decree of judicial dissolution;
    (f) Failure of remaining partners to purchase a Departing Partner's interest as per Section 8.5, if they elect dissolution.
9.2 Liquidation: Upon dissolution, the Partnership shall cease carrying on business except as necessary for winding up its affairs. The Partners (or a designated liquidating Partner/trustee) shall proceed with reasonable promptness to liquidate the Partnership's assets.
9.3 Distribution of Assets: The proceeds from liquidation shall be applied in the following order of priority:
    (a) To pay debts and liabilities of the Partnership owed to third-party creditors;
    (b) To pay debts and liabilities owed to Partners other than for capital and profits;
    (c) To repay Partners' capital contributions (adjusted for profits/losses);
    (d) Any remaining amount shall be distributed to the Partners according to their profit-sharing ratios as defined in Section 4.1.

ARTICLE X: DISPUTE RESOLUTION

10.1 Negotiation: In the event of any dispute arising out of or relating to this Agreement, the Partners shall first attempt to resolve the dispute through good faith negotiation among themselves.
10.2 Mediation: If the dispute cannot be resolved through negotiation within thirty (30) days, the Partners agree to attempt to resolve the dispute through mediation administered by a mutually agreed-upon mediator before resorting to arbitration or litigation.
10.3 Arbitration (Optional): [If the Partners prefer arbitration over court litigation, include:] If mediation is unsuccessful, any controversy or claim arising out of or relating to this Agreement, or the breach thereof, shall be settled by binding arbitration administered in [Specify City, e.g., San Jose Del Monte, Bulacan] in accordance with the arbitration rules of [Specify Body, e.g., the Philippine Dispute Resolution Center, Inc. (PDRCI)], and judgment upon the award rendered by the arbitrator(s) may be entered in any court having jurisdiction thereof.
10.4 Governing Law: This Agreement shall be governed by and construed in accordance with the laws of the Republic of the Philippines.

ARTICLE XI: MISCELLANEOUS

11.1 Notices: Any notice required or permitted under this Agreement shall be in writing and shall be deemed delivered when personally delivered, sent by reputable overnight courier, or sent by registered or certified mail, return receipt requested, postage prepaid, to the addresses of the Partners set forth herein or to such other address as a Partner may designate in writing. Email notice shall be sufficient if receipt is acknowledged.
11.2 Entire Agreement: This Agreement (including Exhibit A) constitutes the entire agreement among the Partners concerning the subject matter hereof and supersedes all prior agreements, understandings, negotiations, and discussions, whether oral or written.
11.3 Amendments: This Agreement may be amended only by a written instrument signed by all Partners.
11.4 Binding Effect: This Agreement shall be binding upon and inure to the benefit of the Partners and their respective heirs, executors, administrators, successors, and permitted assigns.
11.5 Severability: If any provision of this Agreement is held to be invalid, illegal, or unenforceable, the validity, legality, and enforceability of the remaining provisions shall not in any way be affected or impaired thereby.
11.6 Counterparts: This Agreement may be executed in one or more counterparts, each of which shall be deemed an original, but all of which together shall constitute one and the same instrument.

IN WITNESS WHEREOF, the Partners have executed this General Partnership Agreement as of the Effective Date first written above.


(Signature Blocks Placeholder - Add manually or modify script for lines)

_________________________        _________________________
Stella Marie B. Abanono           Nathaniel G. Bingco
(Printed Name)                       (Printed Name)

_________________________        _________________________
Samantha Jane S. Darullo      Louize Christopher S. Galang
(Printed Name)                       (Printed Name)

_________________________        _________________________
Yuri B. Gatbunton                 Neil Vincent E. Jaen
(Printed Name)                       (Printed Name)

_________________________
Myke Jonard S. Sentillas
(Printed Name)


EXHIBIT A

INITIAL CAPITAL CONTRIBUTIONS

As of the Effective Date of the General Partnership Agreement of Drip-o-matic:

| Partner Name                 | Description of Contribution             | Agreed Value (PHP) |
| :--------------------------- | :-------------------------------------- | :----------------- |
| Stella Marie B. Abanono      | [e.g., Cash, Equipment, Marketing Plan] | [PHP Amount]       |
| Nathaniel G. Bingco        | [e.g., Cash, HR Setup Services]         | [PHP Amount]       |
| Samantha Jane S. Darullo   | [e.g., Cash, Financial Model]           | [PHP Amount]       |
| Louize Christopher S. Galang | [e.g., Cash, Prototype Components, Code] | [PHP Amount]       |
| Yuri B. Gatbunton            | [e.g., Cash, Business Plan Concept]     | [PHP Amount]       |
| Neil Vincent E. Jaen         | [e.g., Cash, Operational Workflow]      | [PHP Amount]       |
| Myke Jonard S. Sentillas     | [e.g., Cash, Sales Strategy]            | [PHP Amount]       |
| TOTAL                    |                                         | [PHP Total]    |

*Note: This Exhibit needs to be filled out based on what the partners actually agree to contribute.*
"""

# PDF Generation Settings
TITLE = "GENERAL PARTNERSHIP AGREEMENT"
SUBTITLE = "OF\nDRIP-O-MATIC"
OUTPUT_FILENAME = "Drip-o-matic_Partnership_Agreement.pdf"
FONT_REGULAR = 'Arial'
FONT_BOLD = 'Arial' # 'B' style will be added later
FONT_SIZE_TITLE = 16
FONT_SIZE_SUBTITLE = 14
FONT_SIZE_HEADING = 12
FONT_SIZE_BODY = 10
LINE_HEIGHT_BODY = 5 # in mm
LINE_HEIGHT_HEADING = 7 # in mm

# Create PDF object
pdf = FPDF('P', 'mm', 'A4') # Portrait, millimeters, A4 size
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15) # Auto page break with 15mm margin

# --- Add Content ---

# Title
pdf.set_font(FONT_BOLD, 'B', FONT_SIZE_TITLE)
pdf.cell(0, 10, TITLE, 0, 1, 'C') # width=0 (full), height=10, border=0, ln=1 (next line), align='C'
pdf.ln(5) # Add some space

# Subtitle
pdf.set_font(FONT_BOLD, 'B', FONT_SIZE_SUBTITLE)
pdf.multi_cell(0, 7, SUBTITLE, 0, 'C') # Multi-cell for potential line breaks
pdf.ln(10) # Add more space

# Body Text Processing
pdf.set_font(FONT_REGULAR, '', FONT_SIZE_BODY) # Set default body font
lines = agreement_text.strip().split('\n')

# Skip the title/subtitle lines already added
start_index = 0
for i, line in enumerate(lines):
    if "Effective Date" in line:
        start_index = i
        break

# Process the rest of the lines
for line in lines[start_index:]:
    line = line.strip() # Remove leading/trailing whitespace
    if not line: # Skip empty lines in text, add space in PDF
        pdf.ln(LINE_HEIGHT_BODY / 2)
        continue

    # Basic Heuristic for Headings (adjust if needed)
    is_heading = (
        line.isupper() and len(line.split()) < 5 and not line.startswith(('(', '|', '*', '[', '_')) or # All caps short lines
        line.startswith("ARTICLE ") or
        line.startswith("EXHIBIT A") or
        line.startswith("IN WITNESS WHEREOF")
    )
    is_subheading = line.endswith(':') and (line[0].isdigit() and '.' in line[:4]) # e.g., 1.1 Formation:

    if is_heading:
        pdf.ln(LINE_HEIGHT_HEADING / 2) # Space before heading
        pdf.set_font(FONT_BOLD, 'B', FONT_SIZE_HEADING)
        pdf.multi_cell(0, LINE_HEIGHT_HEADING, line, 0, 'L')
        pdf.set_font(FONT_REGULAR, '', FONT_SIZE_BODY) # Reset to body font
        pdf.ln(LINE_HEIGHT_BODY / 3) # Space after heading
    elif is_subheading:
        pdf.ln(LINE_HEIGHT_BODY / 2)
        pdf.set_font(FONT_BOLD, 'B', FONT_SIZE_BODY) # Bold subheading
        pdf.multi_cell(0, LINE_HEIGHT_BODY, line, 0, 'L')
        pdf.set_font(FONT_REGULAR, '', FONT_SIZE_BODY) # Reset font
    elif line.startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '    *','(a)','(b)','(c)','(d)','(e)','(f)','(i)','(ii)','(iii)','(iv)','(v)','(vi)','(vii)','(viii)')):
        pdf.set_x(pdf.l_margin + 5) # Indent list items slightly
        pdf.multi_cell(0, LINE_HEIGHT_BODY, line, 0, 'L')
        pdf.set_x(pdf.l_margin) # Reset indentation
    elif line.startswith('|') and '---' not in line: # Basic table handling for Exhibit A
         # Simple way: treat table lines as preformatted text
         pdf.set_font('Courier', '', FONT_SIZE_BODY -1) # Use monospace for alignment
         pdf.multi_cell(0, LINE_HEIGHT_BODY, line, 0, 'L')
         pdf.set_font(FONT_REGULAR, '', FONT_SIZE_BODY) # Reset font
    elif line.startswith('___'): # Signature lines
        pdf.ln(3) # Add space before signature lines
        pdf.multi_cell(0, LINE_HEIGHT_BODY, line, 0, 'L')
        pdf.ln(3) # Add space after signature lines
    else:
        # Regular paragraph text
        pdf.multi_cell(0, LINE_HEIGHT_BODY, line, 0, 'L') # width=0 (auto width), height=5mm

# --- Save the PDF ---
try:
    pdf.output(OUTPUT_FILENAME)
    print(f"Successfully created '{OUTPUT_FILENAME}'")
except Exception as e:
    print(f"Error creating PDF: {e}")