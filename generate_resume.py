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
        self.set_auto_page_break(auto=True, margin=12)
        
    def header_section(self, name, title, contact_info):
        """Create executive-style header"""
        # Name with strong presence
        self.set_font('Helvetica', 'B', 22)
        self.set_text_color(20, 60, 100)
        self.cell(0, 10, name, new_x="LMARGIN", new_y="NEXT", align='C')
        
        # Title
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(60, 60, 60)
        self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT", align='C')
        
        # Contact info
        self.set_font('Helvetica', '', 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 5, contact_info, new_x="LMARGIN", new_y="NEXT", align='C')
        
        # Separator line
        self.ln(3)
        self.set_draw_color(20, 60, 100)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        
    def section_title(self, title):
        """Create section title with professional styling"""
        self.ln(2)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(20, 60, 100)
        self.cell(0, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(20, 60, 100)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)
        
    def add_summary(self, summary):
        """Add professional summary"""
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 4.5, summary)
        self.ln(1)
        
    def add_experience(self, title, company, location, period, achievements):
        """Add work experience with strong visual hierarchy"""
        # Job title
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(20, 20, 20)
        self.cell(145, 5, title, new_x="RIGHT", new_y="TOP")
        
        # Period
        self.set_font('Helvetica', '', 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 5, period, new_x="LMARGIN", new_y="NEXT", align='R')
        
        # Company
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(20, 60, 100)
        self.cell(0, 4, f"{company} | {location}", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        
        # Achievements
        self.set_font('Helvetica', '', 9)
        self.set_text_color(30, 30, 30)
        left_margin = self.l_margin
        for achievement in achievements:
            self.set_left_margin(left_margin + 4)
            self.set_x(left_margin + 4)
            self.multi_cell(0, 4.2, f">> {achievement}")
        self.set_left_margin(left_margin)
        self.ln(2)
        
    def add_skills_compact(self, skills_dict):
        """Add skills in compact professional inline format with proper alignment"""
        original_left_margin = self.l_margin
        right_margin = self.r_margin
        page_width = self.w - original_left_margin - right_margin
        category_width = 48
        skills_start_x = original_left_margin + category_width
        skills_width = page_width - category_width
        
        for category, skills in skills_dict.items():
            # Category label (bold, blue)
            self.set_font('Helvetica', 'B', 9)
            self.set_text_color(20, 60, 100)
            self.set_x(original_left_margin)
            self.cell(category_width, 4.5, f"{category}:")
            
            # Skills text (normal, dark) - aligned properly
            self.set_font('Helvetica', '', 9)
            self.set_text_color(30, 30, 30)
            # Temporarily adjust left margin so wrapped text aligns
            self.set_left_margin(skills_start_x)
            self.multi_cell(skills_width, 4.5, skills)
            # Restore original margin
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


def generate_resume():
    """Generate the professional resume PDF"""
    pdf = ResumePDF()
    pdf.add_page()
    
    # ===== HEADER =====
    pdf.header_section(
        name="SAGAR CHAVAN",
        title="Senior Technical Lead - DevOps",
        contact_info="Pune, India  |  sagarchavan6210@gmail.com  |  linkedin.com/in/sagarchavan  |  github.com/saggy6210"
    )
    
    # ===== PROFESSIONAL SUMMARY =====
    pdf.section_title("Professional Summary")
    summary = """Results-driven DevOps Leader with 10+ years of experience architecting enterprise-scale cloud infrastructure, CI/CD pipelines, and platform engineering solutions across AWS and Azure. Proven track record leading cross-functional teams of 5+ engineers, driving DevOps transformation initiatives, and delivering highly available systems with 99.9% uptime SLA. Expert in Infrastructure as Code (Terraform, Ansible), Kubernetes orchestration, comprehensive observability platforms (Grafana, Prometheus, Datadog), and SRE best practices. Demonstrated success in reducing deployment lead times by 60%, achieving 25% infrastructure cost optimization, and implementing enterprise disaster recovery strategies. Passionate about fostering DevOps culture, mentoring engineering teams, and operational excellence."""
    pdf.add_summary(summary)
    
    # ===== CORE COMPETENCIES =====
    pdf.section_title("Core Competencies")
    skills = {
        "Cloud & Infrastructure": "AWS (EKS, EC2, Lambda, RDS, S3, VPC, IAM), Azure (AKS, VMs, App Service), Multi-Cloud Architecture",
        "IaC & Automation": "Terraform, Ansible, CloudFormation, Python, Golang, PowerShell, Shell Scripting",
        "CI/CD & DevOps": "GitLab CI/CD, Jenkins, Azure DevOps, Bitbucket Pipelines, GitHub Actions, ArgoCD",
        "Containers & Orchestration": "Kubernetes, Docker, Helm, EKS, AKS, Container Security, Microservices",
        "Observability & SRE": "Grafana, Prometheus, Alertmanager, Datadog, Elasticsearch, PagerDuty, SLO/SLI/SLA",
        "Leadership & Practices": "Team Leadership (5+ Engineers), Agile/Scrum, DR Planning, Cost Optimization, Security Hardening"
    }
    pdf.add_skills_compact(skills)
    
    # ===== PROFESSIONAL EXPERIENCE =====
    pdf.section_title("Professional Experience")
    
    # CloudHedge - Current Role (Combined with enhanced responsibilities)
    pdf.add_experience(
        title="Senior Technical Lead - DevOps",
        company="CloudHedge Technologies",
        location="Pune, India",
        period="Jul 2019 - Present",
        achievements=[
            "Lead a team of 5+ DevOps engineers, establishing best practices, conducting code reviews, and driving continuous improvement initiatives across enterprise product lines",
            "Architected multi-cloud infrastructure on AWS and Azure using Terraform, managing 200+ resources with zero-downtime deployments and automated disaster recovery procedures",
            "Designed and implemented enterprise CI/CD pipelines using GitLab, Jenkins, Azure DevOps, and Bitbucket, improving deployment frequency by 40% and reducing lead time by 60%",
            "Built comprehensive observability platform using Grafana, Prometheus, Alertmanager, and Datadog with Slack/Teams integrations, achieving 99.9% uptime SLA and reducing MTTR by 50%",
            "Implemented AWS Landing Zone architecture with Transit Gateway, VPC peering, IAM/OIDC, and enterprise security controls for multi-account governance",
            "Automated infrastructure operations using Golang, Python, Ansible, and PowerShell, reducing manual interventions by 80% and provisioning time from 4 hours to 30 minutes",
            "Deployed Kubernetes monitoring stack with custom alerting, Node Exporter, and FlexLM Exporter for license server monitoring across distributed systems",
            "Led disaster recovery planning and implementation including automated backups, certificate/password rotation, and infrastructure resilience testing",
            "Configured GitLab Runners on ESX servers for automated software installation, patching, and configuration management across enterprise environments",
            "Implemented cost optimization strategies through automated resource cleanup, right-sizing, and scheduled shutdown policies, achieving 25% infrastructure cost reduction",
            "Drove cloud-native migration initiatives, containerizing monolithic applications and implementing microservices architecture patterns"
        ]
    )
    
    # Siemens
    pdf.add_experience(
        title="DevOps Engineer",
        company="Siemens Industry Software (MindSphere IoT Platform)",
        location="Pune, India",
        period="Nov 2017 - Jul 2019",
        achievements=[
            "Engineered fully automated CI/CD pipelines with blue-green deployment strategy for Azure Web Apps, reducing deployment failures by 70%",
            "Provisioned Azure infrastructure using Terraform including AKS, VMs, App Service, Functions, Scale Sets, ACR, Redis, SQL DB, and networking components",
            "Designed centralized logging and monitoring solution using ELK Stack, Grafana, Azure Monitor, Log Analytics, and PagerDuty integration, reducing incident response time by 40%",
            "Implemented Kubernetes orchestration with Docker containerization, GitLab Runner automation, and backup/restore procedures for production workloads",
            "Developed Shell and Python automation scripts for deployment orchestration, environment provisioning, and operational efficiency improvements",
            "Established repository management standards, RBAC policies, and security best practices for enterprise code collaboration"
        ]
    )
    
    # Amdocs
    pdf.add_experience(
        title="Technology Integration Engineer",
        company="Amdocs Development Center",
        location="Pune, India",
        period="Jan 2016 - Nov 2017",
        achievements=[
            "Administered WebLogic application servers including deployment automation, performance tuning, and troubleshooting for telecom billing applications serving millions of subscribers",
            "Developed server monitoring tools and automated reporting dashboards for proactive infrastructure management",
            "Created Shell scripting automation for deployment orchestration, reducing manual deployment time by 60%",
            "Provided 24x7 production support ensuring environment stability and rapid incident resolution for mission-critical systems"
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
    
    # Save the PDF
    output_file = "SagarChavan_Resume.pdf"
    pdf.output(output_file)
    print(f"Resume generated successfully: {output_file}")
    return output_file


if __name__ == "__main__":
    generate_resume()
