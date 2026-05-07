import sys

new_content = """    <style>
        /* Animated Elements */
        .anim-float { animation: floatAnim 6s ease-in-out infinite; }
        @keyframes floatAnim {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-15px) rotate(1deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }

        .pulse-glow-box {
            background: var(--medical-blue);
            opacity: 0.2;
            filter: blur(40px);
            animation: pulseGlow 4s linear infinite;
            transform: translate(-50%, -50%) scale(0.9);
        }
        @keyframes pulseGlow {
            0% { transform: translate(-50%, -50%) scale(0.9); opacity: 0.2; }
            50% { transform: translate(-50%, -50%) scale(1.1); opacity: 0.4; }
            100% { transform: translate(-50%, -50%) scale(0.9); opacity: 0.2; }
        }

        .hover-lift { transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease; }
        .hover-lift:hover { transform: translateY(-15px); box-shadow: var(--shadow-lg); }

        .process-line {
            top: 40px; left: 12.5%; width: 75%; height: 3px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
            background-size: 200% 100%;
            animation: flowDash 3s linear infinite;
            z-index: 1;
        }
        @keyframes flowDash { 0% { background-position: 100% 0; } 100% { background-position: -100% 0; } }

        .spin-border-anim { position: relative; box-shadow: 0 0 0 5px rgba(255,255,255,0.2); transition: all 0.5s ease; }
        .spin-border-anim::before {
            content: ''; position: absolute;
            top: -8px; left: -8px; right: -8px; bottom: -8px;
            border: 2px dashed rgba(255,255,255,0.6); border-radius: 50%;
            animation: spinRotate 10s linear infinite;
        }
        @keyframes spinRotate { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .process-icon:hover { transform: scale(1.1); box-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }

        .glow-hover { transition: all 0.4s ease; border: 1px solid transparent; }
        .glow-hover:hover { border-color: var(--medical-blue); box-shadow: 0 10px 40px rgba(37, 99, 235, 0.15); transform: translateY(-5px); }

        .anim-fade-in-left { animation: fadeInLeft 1s ease forwards; }
        .anim-fade-in-up { animation: fadeInUp 1s ease backwards; }
        .anim-fade-in-down { animation: fadeInDown 1s ease forwards; }
        .anim-scale-up { animation: scaleUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) backwards; }

        @keyframes fadeInLeft { from { opacity: 0; transform: translateX(-50px); } to { opacity: 1; transform: translateX(0); } }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-50px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes scaleUp { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }
    </style>

    <!-- SECTION 1: Mission & Philosophy -->
    <section class="py-5 mission-section position-relative overflow-hidden">
        <div class="position-absolute top-0 end-0 p-5 opacity-10">
            <i class="bi bi-shield-plus" style="font-size: 20rem; color: var(--medical-blue);"></i>
        </div>
        <div class="container py-5">
            <div class="row align-items-center g-5">
                <div class="col-lg-6 anim-fade-in-left">
                    <div class="section-title text-start mb-4">
                        <span>Our Mission</span>
                        <h2 class="display-5 fw-bold">Translating Complex Science into Impactful Clarity</h2>
                    </div>
                    <p class="lead text-muted mb-4">We bridge the gap between clinical data and regulatory success.</p>
                    <ul class="list-unstyled mb-5">
                        <li class="mb-3 d-flex align-items-center gap-3"><i class="bi bi-check2-circle fs-4 text-success"></i> <span>100% adherence to global compliance standards</span></li>
                        <li class="mb-3 d-flex align-items-center gap-3"><i class="bi bi-check2-circle fs-4 text-success"></i> <span>Rigorous scientific validation</span></li>
                        <li class="mb-3 d-flex align-items-center gap-3"><i class="bi bi-check2-circle fs-4 text-success"></i> <span>Clear, concise, and compelling narratives</span></li>
                    </ul>
                </div>
                <div class="col-lg-6 position-relative">
                    <div class="image-wrapper anim-float">
                        <img src="assets/images/hero.png" class="img-fluid rounded-4 shadow-lg border border-5 border-white" style="position: relative; z-index: 2;">
                        <!-- Pulse glow behind image -->
                        <div class="pulse-glow-box position-absolute top-50 start-50 translate-middle w-100 h-100 rounded-4" style="z-index: 1;"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 2: Core Accreditations -->
    <section class="py-5 bg-light accreditations-section">
        <div class="container py-5">
            <div class="section-title text-center">
                <span>Standards & Accreditations</span>
                <h2>Global Regulatory Alignment</h2>
            </div>
            <div class="row g-4 mt-4">
                <div class="col-md-4 anim-scale-up" style="animation-delay: 0.1s;">
                    <div class="premium-card text-start h-100 p-4 border-top border-4 border-primary hover-lift">
                        <div class="icon-box bg-soft-blue text-primary rounded-circle mb-4 d-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                            <i class="bi bi-globe fs-3"></i>
                        </div>
                        <h4>ICH-GCP Compliant</h4>
                        <p class="text-muted small">All clinical documents ensure full compliance with the highest international standards of clinical research.</p>
                    </div>
                </div>
                <div class="col-md-4 anim-scale-up" style="animation-delay: 0.3s;">
                    <div class="premium-card text-start h-100 p-4 border-top border-4 border-success hover-lift">
                        <div class="icon-box bg-success bg-opacity-10 text-success rounded-circle mb-4 d-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                            <i class="bi bi-check-circle fs-3"></i>
                        </div>
                        <h4>EU MDR 2017/745</h4>
                        <p class="text-muted small">Specialized expertise in navigating the complex new European Medical Device Regulation landscape.</p>
                    </div>
                </div>
                <div class="col-md-4 anim-scale-up" style="animation-delay: 0.5s;">
                    <div class="premium-card text-start h-100 p-4 border-top border-4 border-info hover-lift">
                        <div class="icon-box bg-info bg-opacity-10 text-info rounded-circle mb-4 d-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                            <i class="bi bi-file-earmark-medical fs-3"></i>
                        </div>
                        <h4>FDA Submissions</h4>
                        <p class="text-muted small">Experienced in FDA-ready documentation formats spanning NDAs, INDs, and diverse medical device 510(k)s.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 3: The Workflow -->
    <section class="py-5 process-section text-white position-relative" style="background: var(--primary);">
        <div class="container py-5">
            <div class="section-title text-center text-white mb-5">
                <span class="text-info">How We Work</span>
                <h2 class="text-white">The Precision Workflow</h2>
            </div>
            
            <div class="row position-relative process-steps g-4">
                <div class="process-line d-none d-lg-block position-absolute anim-dash-flow"></div>
                
                <div class="col-lg-3 col-md-6 text-center position-relative anim-fade-in-up" style="animation-delay: 0.1s;">
                    <div class="process-icon mb-4 mx-auto rounded-circle bg-white text-primary d-flex align-items-center justify-content-center fw-bold fs-3 spin-border-anim" style="width: 80px; height: 80px; z-index: 2; position: relative;">1</div>
                    <h4 class="text-white">Discovery</h4>
                    <p class="small opacity-75">Initial briefing and comprehensive data extraction from clinical sources.</p>
                </div>
                
                <div class="col-lg-3 col-md-6 text-center position-relative anim-fade-in-up" style="animation-delay: 0.3s;">
                    <div class="process-icon mb-4 mx-auto rounded-circle bg-white text-primary d-flex align-items-center justify-content-center fw-bold fs-3 spin-border-anim" style="width: 80px; height: 80px; z-index: 2; position: relative;">2</div>
                    <h4 class="text-white">Drafting</h4>
                    <p class="small opacity-75">Developing cohesive scientific narrative aligned with regulatory templates.</p>
                </div>
                
                <div class="col-lg-3 col-md-6 text-center position-relative anim-fade-in-up" style="animation-delay: 0.5s;">
                    <div class="process-icon mb-4 mx-auto rounded-circle bg-white text-primary d-flex align-items-center justify-content-center fw-bold fs-3 spin-border-anim" style="width: 80px; height: 80px; z-index: 2; position: relative;">3</div>
                    <h4 class="text-white">Review</h4>
                    <p class="small opacity-75">Rigorous QC processes, fact-checking, and stakeholder alignments.</p>
                </div>
                
                <div class="col-lg-3 col-md-6 text-center position-relative anim-fade-in-up" style="animation-delay: 0.7s;">
                    <div class="process-icon mb-4 mx-auto rounded-circle bg-white text-primary d-flex align-items-center justify-content-center fw-bold fs-3 spin-border-anim" style="width: 80px; height: 80px; z-index: 2; position: relative;">4</div>
                    <h4 class="text-white">Delivery</h4>
                    <p class="small opacity-75">Final submission-ready documents delivered securely and on time.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 4: Testimonials -->
    <section class="py-5 testimonial-section bg-background">
        <div class="container py-5">
            <div class="row align-items-center mb-5 anim-fade-in-down">
                <div class="col-lg-6">
                    <div class="section-title text-start mb-0">
                        <span>Testimonials</span>
                        <h2>Trusted by Industry Leaders</h2>
                    </div>
                </div>
                <div class="col-lg-6 text-lg-end mt-4 mt-lg-0">
                    <p class="text-muted mb-0">Voices from the frontlines of pharmaceutical innovation and clinical research.</p>
                </div>
            </div>
            
            <div class="row g-4">
                <div class="col-lg-4 col-md-6 anim-scale-up" style="animation-delay: 0.2s;">
                    <div class="premium-card text-start p-4 bg-white position-relative overflow-hidden glow-hover">
                        <i class="bi bi-quote position-absolute top-0 end-0 opacity-10" style="font-size: 8rem; color: var(--medical-blue); transform: translate(20%, -20%);"></i>
                        <div class="d-flex align-items-center gap-3 mb-4">
                            <img src="assets/images/team.png" class="rounded-circle object-fit-cover" width="60" height="60">
                            <div>
                                <h5 class="mb-0">Dr. Sarah Jenkins</h5>
                                <p class="small text-muted mb-0">VP Clinical Operations</p>
                            </div>
                        </div>
                        <p class="fst-italic opacity-75">"Their attention to detail and profound understanding of complex clinical data transformed our submission process. The CERs were flawless and FDA-ready ahead of schedule."</p>
                        <div class="text-warning mt-3">
                            <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                        </div>
                    </div>
                </div>
                
                <div class="col-lg-4 col-md-6 anim-scale-up" style="animation-delay: 0.4s;">
                    <div class="premium-card text-start p-4 bg-white position-relative overflow-hidden glow-hover">
                        <i class="bi bi-quote position-absolute top-0 end-0 opacity-10" style="font-size: 8rem; color: var(--medical-blue); transform: translate(20%, -20%);"></i>
                        <div class="d-flex align-items-center gap-3 mb-4">
                            <img src="assets/images/manuscript.png" class="rounded-circle object-fit-cover" width="60" height="60">
                            <div>
                                <h5 class="mb-0">Marcus Thorne</h5>
                                <p class="small text-muted mb-0">Director of Regulatory Affairs</p>
                            </div>
                        </div>
                        <p class="fst-italic opacity-75">"Navigating EU MDR was an immense challenge until we partnered with MedWrite Pro. Their expertise de-risked our entire portfolio's technical documentation."</p>
                        <div class="text-warning mt-3">
                            <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                        </div>
                    </div>
                </div>
                
                <div class="col-lg-4 col-md-6 anim-scale-up" style="animation-delay: 0.6s;">
                    <div class="premium-card text-start p-4 bg-white position-relative overflow-hidden glow-hover">
                        <i class="bi bi-quote position-absolute top-0 end-0 opacity-10" style="font-size: 8rem; color: var(--medical-blue); transform: translate(20%, -20%);"></i>
                        <div class="d-flex align-items-center gap-3 mb-4">
                            <img src="assets/images/cme.png" class="rounded-circle object-fit-cover" width="60" height="60">
                            <div>
                                <h5 class="mb-0">Dr. Helena Vost</h5>
                                <p class="small text-muted mb-0">Head of Medical Education</p>
                            </div>
                        </div>
                        <p class="fst-italic opacity-75">"The CME modules developed were perfectly structured, balanced, and deeply engaging. Our physician learners gave the content the highest ratings we've ever seen."</p>
                        <div class="text-warning mt-3">
                            <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-half"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open("about.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if "<!-- Professional Bio -->" in line:
        skip = True
        new_lines.append(new_content + "\n")
    if skip and "<!-- Footer (Same as index) -->" in line:
        skip = False
    
    if not skip:
        new_lines.append(line)

with open("about.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
