from fpdf import FPDF

qa_data = [
    ("2a) Mention in detail the barriers and the strategies of effective listening.",
     "- Barriers: Physical (noise), Psychological (emotions, boredom), Language (jargon), Cultural, Interruptions.\n"
     "- Strategies: Be present, Active listening, Avoid judging, Clarify doubts, Control emotions, Improve language skills."),

    ("2b) Write a paragraph in about 300 words on the topic: Generation Gap.",
     "- Generation gap is the difference in values, ideas, and lifestyles between generations.\n"
     "- Caused by tech, changing culture, education.\n"
     "- Older generations value discipline; younger value freedom.\n"
     "- Can be resolved by empathy, communication, and respect."),

    ("3a) Explain the nature of Technical Communication and how it differs from General communication.",
     "- Technical Communication: Factual, formal, task-focused (e.g. manuals).\n"
     "- General Communication: Informal, expressive, casual.\n"
     "- Differences: Purpose, tone, audience, content style."),

    ("3b) Mention the skills required for a successful technical writer.",
     "- Clear writing, technical knowledge, audience awareness, grammar, organization, research, editing, tool usage."),

    ("4a) Write in detail the salient features and significance of Report writing.",
     "- Features: Objective, formal, structured, concise, uses visuals.\n"
     "- Significance: Aids decision-making, documents info, shows professionalism."),

    ("4b) Explain briefly the purpose and types of Proposal.",
     "- Purpose: To suggest a plan for approval/funding.\n"
     "- Types: Solicited, Unsolicited, Internal, External, Business, Research."),

    ("5a) Briefly, explain and differentiate: Bio-data, Resume and Curriculum Vitae.",
     "- Bio-data: Personal + career info (often for marriage/government).\n"
     "- Resume: Short, tailored for job.\n"
     "- CV: Detailed academic & professional history."),

    ("5b) Elucidate the characteristic features of an email along with its pros and cons.",
     "- Features: Subject, greeting, body, sign-off.\n"
     "- Pros: Fast, convenient, recordable.\n"
     "- Cons: Can be misunderstood, spam issues."),

    ("6a) Prepare a Resume and Cover letter in response to an advertisement.",
     "- Resume: Contact info, career objective, skills, education, experience.\n"
     "- Cover Letter: Address recipient, intro, highlight suitability, closing statement."),

    ("7a) Discuss the skills required for successful Group Discussion.",
     "- Communication, listening, leadership, clarity, teamwork, body language, staying on topic."),

    ("7b) Describe how to project a positive image during an interview.",
     "- Dress well, confident body language, good eye contact, clear speech, polite attitude, research company."),

    ("8a) Explain the role of Non-Verbal Communication Skills in Group Discussion and Interview.",
     "- Shows confidence, attentiveness, and respect.\n"
     "- Includes: eye contact, posture, gestures, facial expressions, tone.\n"
     "- Helps in building rapport and impression.")
]

# PDF setup
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, "Communicative English - Revision Questions & Answers", ln=True, align="C")
pdf.ln(5)
pdf.set_font("Arial", size=11)

for question, answer in qa_data:
    pdf.set_font("Arial", 'B', 11)
    pdf.multi_cell(0, 10, question)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, answer)
    pdf.ln(3)

pdf.output("Communicative_English_Revision_QA.pdf")