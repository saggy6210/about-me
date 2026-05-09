#!/usr/bin/env python3
"""
Resume Generator for Sagar Chavan
Generates a professional ATS-friendly PDF resume for DevOps Lead/Manager/SRE/Platform Engineer roles.
Run: python generate_resume.py
Output: SagarChavan_Resume.pdf
"""

from fpdf import FPDF


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        # Professional color scheme
        self.primary_color = (25, 55, 95)      # Deep navy blue
        self.secondary_color = (70, 130, 180)  # Steel blue
        self.accent_color = (0, 128, 128)      # Teal
        self.text_dark = (30, 30, 30)
        self.text_medium = (70, 70, 70)
        self.text_light = (100, 100, 100)
        
    def draw_header_background(self):
        """Draw a subtle gradient-like header background"""
        self.set_fill_color(245, 248, 252)
        self.rect(0, 0, 210, 52, 'F')
        # Accent line at top
        self.set_fill_color(*self.primary_color)
        self.rect(0, 0, 210, 3, 'F')
        
    def header_section(self, name, title, contact_info, highlights=None):
        """Create executive-style header with modern design"""
        self.draw_header_background()
        
        # Name with strong presence
        self.set_y(8)
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(*self.primary_color)
        self.cell(0, 12, name, new_x="LMARGIN", new_y="NEXT", align='C')
        
        # Title with accent styling
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(*self.secondary_color)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT", align='C')
        
        # Contact info with icons representation
        self.set_font('Helvetica', '', 8)
        self.set_text_color(*self.text_medium)
        self.cell(0, 5, contact_info, new_x="LMARGIN", new_y="NEXT", align='C')
        
        # Decorative separator
        self.ln(3)
        self.set_draw_color(*self.primary_color)
        self.set_line_width(0.5)
        center = 105
        self.line(center - 80, self.get_y(), center + 80, self.get_y())
        self.ln(4)
        
        # Highlights section in modular box
        if highlights:
            # Draw highlight box
            box_y = self.get_y()
            self.set_fill_color(240, 248, 255)  # Light blue background
            self.set_draw_color(*self.secondary_color)
            self.set_line_width(0.8)
            box_height = 14
            self.rect(15, box_y, 180, box_height, 'DF')  # Draw filled rect with border
            
            # Highlights text centered in box
            self.set_xy(17, box_y + 2)
            self.set_font('Helvetica', 'B', 7.5)
            self.set_text_color(*self.primary_color)
            self.multi_cell(176, 4, highlights, align='C')
            self.set_y(box_y + box_height + 3)
        
    def section_title(self, title):
        """Create section title with modern professional styling"""
        self.ln(3)
        # Section icon placeholder (text-based)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(*self.primary_color)
        
        # Draw background strip
        y_pos = self.get_y()
        self.set_fill_color(245, 248, 252)
        self.rect(10, y_pos, 190, 7, 'F')
        
        # Left accent bar
        self.set_fill_color(*self.primary_color)
        self.rect(10, y_pos, 3, 7, 'F')
        
        self.set_xy(16, y_pos + 1)
        self.cell(0, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        
    def add_summary(self, summary):
        """Add professional summary with better typography"""
        self.set_font('Helvetica', '', 9)
        self.set_text_color(*self.text_dark)
        # Add subtle left border
        x_start = self.get_x()
        y_start = self.get_y()
        self.set_left_margin(14)
        self.set_x(14)
        self.multi_cell(182, 4.5, summary)
        self.set_left_margin(10)
        self.ln(1)
        
    def add_experience(self, title, company, location, period, achievements):
        """Add work experience with enhanced visual hierarchy"""
        # Check if we need a new page
        if self.get_y() > 250:
            self.add_page()
        
        # Job title with period
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(*self.text_dark)
        self.cell(140, 5, title, new_x="RIGHT", new_y="TOP")
        
        # Period in accent color
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(*self.secondary_color)
        self.cell(0, 5, period, new_x="LMARGIN", new_y="NEXT", align='R')
        
        # Company with location
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(*self.accent_color)
        self.cell(0, 5, f"{company} | {location}", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        
        # Achievements with modern bullet styling
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(*self.text_dark)
        left_margin = self.l_margin
        for achievement in achievements:
            self.set_left_margin(left_margin + 5)
            self.set_x(left_margin + 5)
            # Custom bullet
            self.set_text_color(*self.secondary_color)
            self.cell(4, 4, chr(149), new_x="RIGHT")  # Bullet character
            self.set_text_color(*self.text_dark)
            self.multi_cell(0, 4, achievement)
        self.set_left_margin(left_margin)
        self.ln(2)
        
    def add_skills_compact(self, skills_dict):
        """Add skills in modern card-style format"""
        original_left_margin = self.l_margin
        page_width = self.w - original_left_margin - self.r_margin
        category_width = 50
        skills_start_x = original_left_margin + category_width
        skills_width = page_width - category_width
        
        for category, skills in skills_dict.items():
            # Category label with accent
            self.set_font('Helvetica', 'B', 9)
            self.set_text_color(*self.primary_color)
            self.set_x(original_left_margin)
            self.cell(category_width, 5, f"{category}:")
            
            # Skills text
            self.set_font('Helvetica', '', 8.5)
            self.set_text_color(*self.text_dark)
            self.set_left_margin(skills_start_x)
            self.multi_cell(skills_width, 5, skills)
            self.set_left_margin(original_left_margin)
        self.ln(1)
        
    def add_education_compact(self, education_list):
        """Add education in compact format"""
        for edu in education_list:
            self.set_font('Helvetica', 'B', 9)
            self.set_text_color(20, 20, 20)
            self.cell(130, 4.5, edu['degree'], new_x="RIGHT", new_y="TOP")
            self.set_font('Helvetica', '', 8)
            self.set_text_color(80, 80, 80)
            self.cell(0, 4.5, edu['period'], new_x="LMARGIN", new_y="NEXT", align='R')
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(60, 60, 60)
            self.cell(0, 4, edu['institution'], new_x="LMARGIN", new_y="NEXT")
            self.ln(1)
    
    def add_awards(self, awards):
        """Add awards section"""
        self.set_font('Helvetica', '', 9)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 4.2, awards)


def generate_resume():
    """Generate the professional resume PDF"""
    pdf = ResumePDF()
    pdf.add_page()
    
    # ===== HEADER =====
    pdf.header_section(
        name="SAGAR CHAVAN",
        title="Senior Technical Lead - DevOps",
        contact_info="Pune, India  |  sagarchavan6210@gmail.com  |  linkedin.com/in/sagarchavan  |  +91-8308001062  |  saggy6210.github.io/about-me/",
        highlights="10+ Years DevOps & Cloud Engineering Experience | DevOps Leader | AI-Assisted Development using Visual Studio Copilot\nPTC India AI Hackathon Winner | Cross-Functional Team Leadership & Mentoring | DevOps Transformation Initiatives"
    )
    
    # ===== PROFESSIONAL SUMMARY =====
    pdf.section_title("Professional Summary")
    summary = """Results-driven DevOps Leader with 10+ years of experience in designing, automating, and managing enterprise-scale cloud infrastructure and DevOps platforms across AWS and Azure environments. Expertise in Infrastructure as Code (Terraform, Ansible), container orchestration (Kubernetes, Helm), CI/CD automation (Jenkins, GitLab CI/CD, Bitbucket, GitHub Actions), observability and monitoring platforms (Datadog, Grafana, Prometheus, Elasticsearch, Alertmanager), cloud-native technologies (Docker, AWS, Azure), and SRE best practices.

Strong hands-on experience with Terraform, Ansible, Docker, Kubernetes, Jenkins, GitLab, Bitbucket, Helm, Prometheus, Grafana, Elasticsearch, Datadog, Linux, Windows, Shell scripting, Python, and GoLang. Proven ability to architect scalable, highly available, and secure infrastructure solutions while improving operational efficiency and deployment reliability.

Proven track record leading cross-functional teams of 5+ engineers, driving DevOps transformation initiatives, and delivering highly available systems with 99.9% uptime SLA. Experienced in leading and mentoring teams of 4-5 engineers, implementing SRE and monitoring best practices, and automating enterprise deployment workflows. Successfully delivered cloud cost optimization initiatives, centralized logging and monitoring platforms, automated infrastructure provisioning, and application deployment pipelines.

Passionate about innovation and AI-driven engineering solutions, with hands-on experience using GitHub Copilot and Visual Studio Copilot for development acceleration and automation. Recognized for mentoring and leading a team that won the PTC India-level AI Hackathon, demonstrating strong leadership, collaboration, and problem-solving capabilities in AI and automation initiatives.

Skilled in developing customer-focused internal web applications and dashboards for operational tracking, proactive issue identification, and log analytics using Datadog, Grafana, and Prometheus. Actively involved in building internal mentoring programs to strengthen cloud, automation, and consulting competencies within engineering teams."""
    pdf.add_summary(summary)
    
    # ===== CORE COMPETENCIES =====
    pdf.section_title("Core Competencies")
    skills = {
        "Cloud & Infrastructure": "AWS (EKS, EC2, S3, VPC, IAM), Azure (AKS, VMs, Batch Account, Gallery Images, Storage Accounts)",
        "IaC & Automation": "Terraform, Ansible, Python, Golang, PowerShell, Shell Scripting",
        "CI/CD & DevOps": "GitLab CI/CD, Jenkins, Bitbucket Pipelines, GitHub Actions",
        "Containers & Orchestration": "Kubernetes, Docker, Helm, EKS, AKS, Container Security, Microservices",
        "Observability & SRE": "Grafana, Prometheus, Alertmanager, Datadog, Elasticsearch, PagerDuty, SLO/SLI/SLA",
        "Leadership & Practices": "Team Leadership (5+ Engineers), Agile/Scrum, DR Planning, Cost Optimization, Security Hardening"
    }
    pdf.add_skills_compact(skills)
    
    # ===== PROFESSIONAL EXPERIENCE =====
    pdf.section_title("Professional Experience")
    
    # PTC Software
    pdf.add_experience(
        title="Senior Technical Lead - DevOps",
        company="PTC Software",
        location="Pune, India",
        period="May 2022 - Present",
        achievements=[
            "Developing and executing DevOps strategies that enhances collaboration between DevOps, Dev and QA teams by actively seeking input, documenting processes, and ensuring that decisions are well-informed and aligned with all stakeholders",
            "Leading and mentoring a team of DevOps engineers, guiding best practices, fostering an innovative team culture, and supporting the team in debugging and investigating production issues for resolution",
            "Implementing and managing DevOps tools and technologies to automate processes including CI/CD using Gitlab, Python, Ansible playbooks, Terraform for IaC, Grafana, and Datadog dashboards for monitoring",
            "Led automation of Azure gallery image creation process by evaluating requirements and implementation using Ansible, Python, Azure Identity, Project infrastructure management, license server setup and monitoring",
            "Automated pipelines to upload installers to Jfrog artifactory, deployment pipeline, automated regular cleanup to reduce the infrastructure cost",
            "Led the scheduled disaster recovery for VCS project practices",
            "Developed internal GoLang tools for operational automation and cloud resource cleanup",
            "Built automated Azure image creation and Azure Batch deployment solutions",
            "Implemented enterprise monitoring and alerting using Datadog, Grafana, Prometheus, and Alertmanager",
            "Automated FlexLM license server deployment and recurring license management workflows",
            "Managed Kubernetes and Helm-based application deployments across environments",
            "Developed internal static web applications for operational tracking and customer-centric reporting",
            "Built centralized dashboards and log analytics solutions for proactive incident identification",
            "Led mentoring initiatives to improve cloud, automation, and consulting capabilities within engineering teams"
        ]
    )
    
    # CloudHedge
    pdf.add_experience(
        title="DevOps Engineer",
        company="CloudHedge Technologies",
        location="Pune, India",
        period="Jul 2019 - Apr 2022",
        achievements=[
            "Played key role in cloud (AWS/Azure) infrastructure provisioning using Terraform and CI/CD implementation using Jenkins, Gitlab, Bitbucket, and Azure/AWS pipeline",
            "Designed and implemented automated functional and performance testing (sanity, regression) for the CloudHedge Enterprise using Python, Bash, Jenkins, Docker & Rest API",
            "Worked on landing zone setup on AWS. Used AWS services are Route 53, ALB, NLB, EC2, VPC, Transit Gateway, RAM, IAM(Roles, policy, OIDC), API gateway, EKS, ECR, Lambda, RDS (MySql, Postgres Aurora), ElastiCache, DynamoDB, S3, System manager, KMS, AWS backup, ACM",
            "Worked on an application assessment for migration to cloud-native containerization using the CloudHedge tool and Application performance consulting for multiple clients",
            "Reduced monthly cost by $240 by removing unnecessary instances and services and enabling auto-shutdown on non-prod environments"
        ]
    )
    
    # Siemens
    pdf.add_experience(
        title="DevOps Engineer",
        company="Siemens Industry Software (MindSphere IoT Platform)",
        location="Pune, India",
        period="Nov 2017 - Jul 2019",
        achievements=[
            "Successfully created and maintained fully automated CI/CD pipeline & blue green deployment for azure web apps using Gitlab and Jenkins pipeline",
            "Worked on repository management, user-based access, and roles creation, cloud infrastructure provisioning on Azure using terraform. Used Azure services are AKS, VM, App Service, Azure functions, Scale Sets, ACR, Azure Redis, Azure SQL DB, Storage Account, WAF, Virtual Network, Application Gateway, Azure Frontdoor, Key Vault, Azure monitor",
            "Designed and implemented Logging, Monitoring and alerting setup for MindSphere project using Grafana, Elasticsearch, Pagerduty, Azure Application insight, Log Analytics, Azure Monitor, Dashboard, and Alerts",
            "Worked on the environment setup, Micro Services, Docker, AKS, Gitlab runner, Jenkins, backup and restore, automation using shell and python"
        ]
    )
    
    # Amdocs
    pdf.add_experience(
        title="Technology Integration Engineer",
        company="Amdocs Development Center",
        location="Pune, India",
        period="Jan 2016 - Nov 2017",
        achievements=[
            "Worked on WebLogic application server monitoring, configuration, applications deployment, and troubleshooting the functional issues on SIT/UIT environments",
            "Designed and developed a 'Server Monitoring Tool' which shows server healths, capacity, uptime, etc and share the report over the mail",
            "Developed and modified scripts as per the business requirements"
        ]
    )
    
    # Early Career
    pdf.add_experience(
        title="Project Intern",
        company="Persistent Systems",
        location="Pune, India",
        period="Jan 2015 - Jul 2015",
        achievements=[
            "Developed test suite migration software 'Smart Migration Tool for test suite of data warehouse appliance' in Perl Script"
        ]
    )
    
    # ===== EDUCATION =====
    pdf.section_title("Education")
    education = [
        {"degree": "MBA - International Business", "institution": "PUMBA, Savitribai Phule Pune University", "period": "2019 - 2021"},
        {"degree": "B.Tech - Computer Science", "institution": "Walchand College of Engineering, Sangli", "period": "2012 - 2015"},
        {"degree": "Diploma - Information Technology", "institution": "Government Polytechnic, Kolhapur", "period": "2009 - 2012"}
    ]
    pdf.add_education_compact(education)
    
    # ===== AWARDS =====
    pdf.section_title("Awards & Recognition")
    pdf.add_awards("Winner of PTC India Hackathon 2026 & Other Applause Awards")
    
    # Save the PDF
    output_file = "SagarChavan_Resume.pdf"
    pdf.output(output_file)
    print(f"Resume generated successfully: {output_file}")
    return output_file


if __name__ == "__main__":
    generate_resume()
