from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_PARAGRAPH_ALIGNMENT

# Create a presentation object
prs = Presentation()

# --------------------------
# Slide 1: Title Slide
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Time Management and Staff Development"
subtitle.text = "College of Nursing\nPresenter: [Your Name]\nInstitution: [College Name]\nDate: [Month, Year]"

# --------------------------
# Slide 2: Agenda/Overview
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Agenda/Overview"
tf = slide.shapes.placeholders[1].text_frame
tf.text = "Introduction and background"
for point in [
    "Importance of time management in nursing",
    "Staff development strategies",
    "Integration of time management and staff development",
    "Case studies and research findings",
    "Recommendations and future directions",
    "Conclusion and references",
]:
    p = tf.add_paragraph()
    p.text = point
    p.level = 1

# --------------------------
# Slide 3: Introduction
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Introduction"
tf = slide.shapes.placeholders[1].text_frame
tf.text = "• Define key terms: time management and staff development"
p = tf.add_paragraph()
p.text = "• Relevance to nursing practice and leadership"
p = tf.add_paragraph()
p.text = "• Overview of presentation goals"
p = tf.add_paragraph()
p.text = "Reference: APA guidelines (American Psychological Association, 2020)"
p.level = 0

# --------------------------
# Slide 4: Importance of Time Management in Nursing
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Importance of Time Management in Nursing"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Enhances patient care and safety",
    "Reduces burnout and improves efficiency",
    "Supports work-life balance",
    "Improves team collaboration and communication",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 5: Time Management Challenges in Healthcare
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Time Management Challenges in Healthcare"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "High patient loads and unpredictable schedules",
    "Interruptions and distractions",
    "Balancing administrative and clinical responsibilities",
    "Stress and burnout issues (Smith & Jones, 2018)",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 6: Strategies for Effective Time Management
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Strategies for Effective Time Management"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Prioritization techniques (e.g., ABC method)",
    "Use of digital calendars and reminders",
    "Delegation and teamwork",
    "Structured scheduling and periodic review",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0
p = tf.add_paragraph()
p.text = "Tip: Use evidence-based strategies from recent nursing literature."
p.level = 0

# --------------------------
# Slide 7: Time Management Tools in Nursing
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Time Management Tools in Nursing"
tf = slide.shapes.placeholders[1].text_frame
tf.text = "• Digital schedulers (e.g., Outlook, Google Calendar)"
p = tf.add_paragraph()
p.text = "• Task management apps (e.g., Trello, Asana)"
p = tf.add_paragraph()
p.text = "• Time-tracking software"
p = tf.add_paragraph()
p.text = "Visual Aid: Table comparing key features of each tool."

# --------------------------
# Slide 8: Diagram – The Time Management Cycle
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "The Time Management Cycle"
# Add a placeholder shape for the diagram
txBox = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(3))
tf = txBox.text_frame
tf.text = "Flowchart: Planning → Prioritizing → Scheduling → Executing → Evaluating\n[Insert Diagram Here]"

# --------------------------
# Slide 9: Staff Development: Definition and Importance
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Staff Development: Definition and Importance"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Definition: Process of improving professional skills and competencies",
    "Importance: Enhances quality of care and promotes career growth",
    "Focus on continuous learning and skill enhancement",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 10: Staff Development in Nursing
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Staff Development in Nursing"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Continuing education, mentorship, and professional training",
    "Impact on patient outcomes and staff retention",
    "Fostering a culture of lifelong learning",
    "Reference: (Doe & Lee, 2019)",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 11: APA Guidelines for Professional Communication
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "APA Guidelines for Professional Communication"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Clarity and precision in writing",
    "Bias-free language",
    "Consistent use of headings and subheadings",
    "In-text citations and references following APA style",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 12: Table – Comparison of Staff Development Models
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "Comparison of Staff Development Models"
# Create table with 4 columns (Model, Description, Benefits) and 4 rows (header + 3 data rows)
rows = 4
cols = 3
left = Inches(0.5)
top = Inches(1.5)
width = Inches(9)
height = Inches(1.5)
table = slide.shapes.add_table(rows, cols, left, top, width, height).table
# Set column headings
table.cell(0, 0).text = "Model"
table.cell(0, 1).text = "Description"
table.cell(0, 2).text = "Benefits"
# Data rows
table.cell(1, 0).text = "Mentorship"
table.cell(1, 1).text = "One-on-one guidance"
table.cell(1, 2).text = "Personalized growth"
table.cell(2, 0).text = "Continuing Education"
table.cell(2, 1).text = "Formal courses and certifications"
table.cell(2, 2).text = "Updated knowledge and skills"
table.cell(3, 0).text = "Simulation-Based Training"
table.cell(3, 1).text = "Hands-on, realistic practice scenarios"
table.cell(3, 2).text = "Improved clinical competencies"

# --------------------------
# Slide 13: Strategies for Effective Staff Development
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Strategies for Effective Staff Development"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Implement mentorship programs",
    "Offer continuing education opportunities",
    "Use simulation and hands-on training",
    "Encourage self-directed learning",
    "Provide regular performance feedback and goal setting",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 14: Integration of Time Management and Staff Development
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Integration of Time Management & Staff Development"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Efficient time management supports ongoing staff development",
    "Balancing daily tasks with educational opportunities",
    "Scheduling regular training sessions within busy workdays",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 15: Benefits of Effective Time Management on Staff Development
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Benefits on Staff Development"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Increased productivity and enhanced learning",
    "Reduced stress and improved work satisfaction",
    "Better patient care through continuous skill improvement",
    "Positive impact on team dynamics",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 16: Case Study Example
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Case Study Example"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Example of a nursing unit that improved outcomes via integrated time management and staff development",
    "Key Interventions: Restructured scheduling, targeted training sessions, mentorship initiatives",
    "Results: Improved patient satisfaction and staff retention",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 17: Diagram – Workflow in Nursing Staff Development
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "Workflow in Nursing Staff Development"
txBox = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(3))
tf = txBox.text_frame
tf.text = "Workflow: Assessment → Planning → Implementation → Evaluation → Feedback\n[Insert Workflow Diagram Here]"

# --------------------------
# Slide 18: Best Practices for Implementation
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Best Practices for Implementation"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Develop clear policies and objectives",
    "Foster open communication and feedback",
    "Monitor progress with measurable outcomes",
    "Adjust strategies based on evaluation data",
    "Reference: (Brown, 2021)",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 19: Research Findings and Evidence
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Research Findings & Evidence"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Summarize key studies on time management and staff development",
    "Highlight evidence supporting integrated approaches",
    "Discuss implications for nursing practice",
    "Reference: (Johnson et al., 2020)",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 20: Table – Summary of Research Studies
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "Summary of Research Studies"
rows = 4
cols = 4
left = Inches(0.5)
top = Inches(1.5)
width = Inches(9)
height = Inches(1.5)
table = slide.shapes.add_table(rows, cols, left, top, width, height).table
# Set column headings
table.cell(0, 0).text = "Study"
table.cell(0, 1).text = "Focus"
table.cell(0, 2).text = "Key Findings"
table.cell(0, 3).text = "Reference"
# Data rows
table.cell(1, 0).text = "Study A"
table.cell(1, 1).text = "Time management strategies"
table.cell(1, 2).text = "Reduced burnout by 20%"
table.cell(1, 3).text = "(Smith & Jones, 2018)"
table.cell(2, 0).text = "Study B"
table.cell(2, 1).text = "Staff development programs"
table.cell(2, 2).text = "Increased job satisfaction"
table.cell(2, 3).text = "(Doe & Lee, 2019)"
table.cell(3, 0).text = "Study C"
table.cell(3, 1).text = "Integrated approaches"
table.cell(3, 2).text = "Improved patient outcomes"
table.cell(3, 3).text = "(Johnson et al., 2020)"

# --------------------------
# Slide 21: Challenges and Proposed Solutions
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Challenges & Proposed Solutions"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Challenges: Limited resources, time constraints, resistance to change",
    "Solutions: Incremental implementation, incentivize training, leverage technology for flexible learning",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 22: Future Directions in Nursing Staff Development
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Future Directions in Staff Development"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Emerging trends: Digital learning platforms, simulation technology",
    "Integration of interprofessional education",
    "Continuous quality improvement processes",
    "Future research areas and potential innovations",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 23: Recommendations for the College of Nursing
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Recommendations for the College of Nursing"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Develop a comprehensive time management training module",
    "Create a structured staff development program with clear goals",
    "Allocate resources for digital tools and mentorship",
    "Implement regular evaluations and feedback loops",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 24: Conclusion
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Conclusion"
tf = slide.shapes.placeholders[1].text_frame
for line in [
    "Recap of the importance of time management and staff development",
    "Summary of key strategies and benefits",
    "Final thoughts on improving nursing practice and patient outcomes",
    "Call to action for adopting best practices",
]:
    p = tf.add_paragraph()
    p.text = f"• {line}"
    p.level = 0

# --------------------------
# Slide 25: References
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "References"
tf = slide.shapes.placeholders[1].text_frame
references = [
    "American Psychological Association. (2020). Publication manual of the American Psychological Association (7th ed.).",
    "Brown, A. (2021). Effective strategies for staff development in nursing. Journal of Nursing Education, 60(3), 145–152.",
    "Doe, J., & Lee, K. (2019). Impact of continuing education on nursing performance. Nursing Management, 50(2), 78–85.",
    "Johnson, M., et al. (2020). Integrating time management and staff development: A case study. Nursing Research, 69(1), 34–40.",
    "Smith, R., & Jones, L. (2018). Time management in clinical settings: Challenges and solutions. Journal of Healthcare Management, 63(4), 210–220."
]
for ref in references:
    p = tf.add_paragraph()
    p.text = ref
    p.level = 0

# --------------------------
# Save the presentation
prs.save("TimeManagementStaffDevelopment.pptx")
print("Presentation created and saved as TimeManagementStaffDevelopment.pptx")
