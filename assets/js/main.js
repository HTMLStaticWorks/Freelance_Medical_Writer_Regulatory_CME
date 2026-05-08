document.addEventListener('DOMContentLoaded', () => {
    // Sticky Header
    const header = document.querySelector('.header');
    const keepScrolled = header && header.classList.contains('keep-scrolled');

    if (header) {
        if (keepScrolled) {
            header.classList.add('scrolled');
        } else {
            window.addEventListener('scroll', () => {
                if (window.scrollY > 50) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }
            });
        }
    }

    // Dark Mode Toggle
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;

    const enableDarkMode = () => {
        body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'enabled');
        if (darkModeToggle) darkModeToggle.innerHTML = '<i class="bi bi-sun"></i>';
    };

    const disableDarkMode = () => {
        body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'disabled');
        if (darkModeToggle) darkModeToggle.innerHTML = '<i class="bi bi-moon"></i>';
    };

    if (localStorage.getItem('darkMode') === 'enabled') {
        enableDarkMode();
    }

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            if (body.classList.contains('dark-mode')) {
                disableDarkMode();
            } else {
                enableDarkMode();
            }
        });
    }

    // RTL Toggle
    const rtlToggle = document.getElementById('rtlToggle');
    const root = document.documentElement;

    const setRtl = (enabled) => {
        root.setAttribute('dir', enabled ? 'rtl' : 'ltr');
        localStorage.setItem('rtlMode', enabled ? 'enabled' : 'disabled');
    };

    setRtl(localStorage.getItem('rtlMode') === 'enabled');

    if (rtlToggle) {
        rtlToggle.addEventListener('click', () => {
            setRtl(root.getAttribute('dir') !== 'rtl');
        });
    }

    // Mobile Menu
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const mobileNav = document.getElementById('mobileNav');
    const closeMenu = document.getElementById('closeMenu');
    const dashboardToggle = document.querySelector('a[aria-label="Dashboard"]');
    const desktopBreakpoint = 1200;

    const syncHeaderTogglesPlacement = () => {
        if (!darkModeToggle || !rtlToggle || !mobileNav || !mobileMenuToggle) return;

        const headerActions = mobileMenuToggle.parentElement;
        if (!headerActions) return;

        let mobileControls = mobileNav.querySelector('.mobile-nav-controls');
        if (!mobileControls) {
            mobileControls = document.createElement('div');
            mobileControls.className = 'mobile-nav-controls';

            const authActions = mobileNav.querySelector('.mt-4.d-flex.flex-column.gap-3.w-75');
            if (authActions) {
                mobileNav.insertBefore(mobileControls, authActions);
            } else {
                mobileNav.appendChild(mobileControls);
            }
        }

        if (window.innerWidth < desktopBreakpoint) {
            if (dashboardToggle) {
                dashboardToggle.classList.remove('d-none', 'd-xl-inline-flex');
                dashboardToggle.classList.add('d-inline-flex');
                mobileControls.appendChild(dashboardToggle);
            }
            mobileControls.appendChild(darkModeToggle);
            mobileControls.appendChild(rtlToggle);
            return;
        }

        const loginButton = headerActions.querySelector('.btn-outline-premium');
        if (dashboardToggle) {
            dashboardToggle.classList.remove('d-inline-flex');
            dashboardToggle.classList.add('d-none', 'd-xl-inline-flex');
        }
        if (loginButton) {
            if (dashboardToggle) {
                headerActions.insertBefore(dashboardToggle, loginButton);
            }
            headerActions.insertBefore(rtlToggle, loginButton);
            headerActions.insertBefore(darkModeToggle, rtlToggle);
        } else {
            if (dashboardToggle) {
                headerActions.insertBefore(dashboardToggle, mobileMenuToggle);
            }
            headerActions.insertBefore(rtlToggle, mobileMenuToggle);
            headerActions.insertBefore(darkModeToggle, rtlToggle);
        }
    };

    syncHeaderTogglesPlacement();
    window.addEventListener('resize', syncHeaderTogglesPlacement);

    if (mobileMenuToggle && mobileNav) {
        mobileMenuToggle.addEventListener('click', () => {
            mobileNav.classList.add('active');
        });
    }

    if (closeMenu && mobileNav) {
        closeMenu.addEventListener('click', () => {
            mobileNav.classList.remove('active');
        });
    }

    // Back To Top (only on pages that include footer)
    const footer = document.querySelector('.footer');
    if (footer) {
        let backToTop = document.getElementById('backToTop');
        if (!backToTop) {
            backToTop = document.createElement('button');
            backToTop.id = 'backToTop';
            backToTop.className = 'back-to-top';
            backToTop.type = 'button';
            backToTop.setAttribute('aria-label', 'Back to top');
            backToTop.innerHTML = '<i class="bi bi-arrow-up"></i>';
            document.body.appendChild(backToTop);
        }

        const toggleBackToTop = () => {
            if (window.scrollY > 300) {
                backToTop.classList.add('show');
            } else {
                backToTop.classList.remove('show');
            }
        };

        window.addEventListener('scroll', toggleBackToTop);
        toggleBackToTop();

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Animation on Scroll
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.premium-card, .section-title, .hero-content').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.8s ease-out';
        observer.observe(el);
    });

    // Handle the fade-in class manually since we don't use extra libraries
    const style = document.createElement('style');
    style.innerHTML = `
        .fade-in-up {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);
});
