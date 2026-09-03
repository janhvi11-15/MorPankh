from manim import *
import numpy as np

config.background_color = "#01040A"


class MorPankh(MovingCameraScene):

    def construct(self):

        self.add_sound("C:\\Users\\RAVI\\Downloads\\janhvi-portfolio\\janhvi-portfolio\\dpstudiomusic-indian-background-flute-250098.mp3")

        np.random.seed(27)

        # ==========================================================
        # COSMIC WORLD
        # ==========================================================

        stars = self.make_stars()
        nebula = self.make_nebula()

        self.add(nebula)
        self.add(stars)

        # ==========================================================
        # FEATHER
        # ==========================================================

        shaft = self.make_shaft()

        self.play(
            Create(shaft),
            run_time=2.8,
            rate_func=smooth
        )

        # Main feather fibers
        left = self.make_filaments(-1)
        right = self.make_filaments(1)

        self.play(
            LaggedStart(
                *[Create(x) for x in left],
                lag_ratio=0.004
            ),
            run_time=4.5,
            rate_func=smooth
        )

        self.play(
            LaggedStart(
                *[Create(x) for x in right],
                lag_ratio=0.004
            ),
            run_time=4.5,
            rate_func=smooth
        )

        # Fine secondary fibers
        fine_left = self.make_fine_filaments(-1)
        fine_right = self.make_fine_filaments(1)

        self.play(
            LaggedStart(
                *[Create(x) for x in fine_left],
                lag_ratio=0.003
            ),
            LaggedStart(
                *[Create(x) for x in fine_right],
                lag_ratio=0.003
            ),
            run_time=3
        )

        # ==========================================================
        # FEATHER EYE
        # ==========================================================

        eye = self.make_eye()

        self.play(
            LaggedStart(
                *[
                    FadeIn(x, scale=0.88)
                    for x in eye
                ],
                lag_ratio=0.16
            ),
            run_time=3.5,
            rate_func=smooth
        )

        # ==========================================================
        # MICRO PARTICLES
        # ==========================================================

        particles = self.make_particles()

        self.play(
            LaggedStart(
                *[
                    FadeIn(p, scale=0.1)
                    for p in particles
                ],
                lag_ratio=0.005
            ),
            run_time=2
        )

        # ==========================================================
        # COMPLETE FEATHER
        # ==========================================================

        feather = VGroup(
            shaft,
            left,
            right,
            fine_left,
            fine_right,
            eye
        )

        # ==========================================================
        # CINEMATIC CAMERA PUSH
        # ==========================================================

        self.play(
            self.camera.frame.animate
            .scale(0.83)
            .move_to([0, 0.25, 0]),
            run_time=3,
            rate_func=smooth
        )

        # ==========================================================
        # NATURAL SWAY
        # ==========================================================

        self.play(
            feather.animate.rotate(
                0.035,
                about_point=np.array([0, -3.1, 0])
            ),
            run_time=2,
            rate_func=there_and_back
        )

        self.play(
            feather.animate.rotate(
                -0.06,
                about_point=np.array([0, -3.1, 0])
            ),
            run_time=2.5,
            rate_func=there_and_back
        )

        self.wait(2)

        # ==========================================================
        # FINAL HOLD
        # ==========================================================

        self.wait(4)

    # ==============================================================
    # COSMIC STARS
    # ==============================================================

    def make_stars(self):

        stars = VGroup()

        for _ in range(420):

            x = np.random.uniform(-7.2, 7.2)
            y = np.random.uniform(-4.3, 4.3)

            radius = np.random.uniform(
                0.003,
                0.018
            )

            star = Dot(
                [x, y, 0],
                radius=radius,
                color="#BFEFFF"
            )

            star.set_opacity(
                np.random.uniform(0.25, 0.9)
            )

            stars.add(star)

        # Larger distant stars
        for _ in range(22):

            x = np.random.uniform(-6.5, 6.5)
            y = np.random.uniform(-3.8, 3.8)

            star = Dot(
                [x, y, 0],
                radius=np.random.uniform(
                    0.025,
                    0.045
                ),
                color="#D8FAFF"
            )

            stars.add(star)

        return stars

    # ==============================================================
    # SOFT NEBULA
    # ==============================================================

    def make_nebula(self):

        nebula = VGroup()

        for _ in range(18):

            cloud = Ellipse(
                width=np.random.uniform(3.5, 7.5),
                height=np.random.uniform(0.8, 2.4),
                stroke_width=0,
                fill_color="#073C61",
                fill_opacity=np.random.uniform(
                    0.008,
                    0.025
                )
            )

            cloud.rotate(
                np.random.uniform(
                    -0.9,
                    0.9
                )
            )

            cloud.move_to([
                np.random.uniform(-2.8, 2.8),
                np.random.uniform(-1.5, 1.8),
                0
            ])

            nebula.add(cloud)

        return nebula

    # ==============================================================
    # SHAFT
    # ==============================================================

    def make_shaft(self):

        def shaft_curve(t):

            return np.array([
                0.12 * np.sin(0.72 * t)
                + 0.015 * t * t,

                t,

                0
            ])

        shaft = ParametricFunction(
            shaft_curve,
            t_range=[-3.35, 2.7],
            stroke_width=4,
            color="#315044"
        )

        return shaft

    # ==============================================================
    # MAIN FEATHER FILAMENTS
    # ==============================================================

    def make_filaments(self, side):

        group = VGroup()

        # 190 fibers per side
        ys = np.linspace(
            -2.95,
            2.58,
            190
        )

        for i, y in enumerate(ys):

            u = (y + 2.95) / 5.53

            # Feather envelope
            envelope = (
                np.sin(np.pi * u)
                ** 0.58
            )

            # Natural asymmetry
            random_factor = np.random.uniform(
                0.84,
                1.08
            )

            width = (
                0.10
                + 2.35
                * envelope
                * random_factor
            )

            # slight taper toward tip
            width *= (
                1
                - 0.16 * u
            )

            sx = (
                0.12
                * np.sin(0.72 * y)
                + 0.015 * y * y
            )

            # Curved ending
            tx = sx + side * width

            ty = y + np.random.uniform(
                0.16,
                0.44
            )

            bend = np.random.uniform(
                0.05,
                0.30
            )

            lift = np.random.uniform(
                0.01,
                0.08
            )

            def fiber(
                t,
                sx=sx,
                y=y,
                tx=tx,
                ty=ty,
                bend=bend,
                lift=lift,
                side=side
            ):

                return np.array([

                    sx
                    + (tx - sx) * t
                    + side
                    * bend
                    * np.sin(np.pi * t),

                    y
                    + (ty - y) * t
                    + lift
                    * np.sin(np.pi * t),

                    0

                ])

            filament = ParametricFunction(
                fiber,
                t_range=[0, 1],
                stroke_width=np.random.uniform(
                    0.28,
                    0.72
                )
            )

            filament.set_color(
                np.random.choice([
                    "#073C3C",
                    "#084A46",
                    "#07564F",
                    "#0A6258",
                    "#103F4A",
                    "#155B59"
                ])
            )

            filament.set_opacity(
                np.random.uniform(
                    0.38,
                    0.82
                )
            )

            group.add(filament)

        return group

    # ==============================================================
    # ULTRA-FINE SECONDARY FIBERS
    # ==============================================================

    def make_fine_filaments(self, side):

        group = VGroup()

        ys = np.linspace(
            -2.55,
            2.40,
            115
        )

        for y in ys:

            u = (y + 2.55) / 4.95

            width = (
                0.12
                + 2.0
                * np.sin(np.pi * u)
                ** 0.72
            )

            width *= np.random.uniform(
                0.65,
                1.02
            )

            sx = (
                0.12
                * np.sin(0.72 * y)
                + 0.015 * y * y
            )

            tx = sx + side * width

            ty = y + np.random.uniform(
                0.12,
                0.32
            )

            bend = np.random.uniform(
                0.03,
                0.18
            )

            def fine_curve(
                t,
                sx=sx,
                y=y,
                tx=tx,
                ty=ty,
                bend=bend,
                side=side
            ):

                return np.array([

                    sx
                    + (tx - sx) * t
                    + side
                    * bend
                    * np.sin(np.pi * t),

                    y
                    + (ty - y) * t,

                    0

                ])

            fiber = ParametricFunction(
                fine_curve,
                t_range=[0, 1],
                stroke_width=np.random.uniform(
                    0.15,
                    0.38
                ),
                stroke_opacity=np.random.uniform(
                    0.22,
                    0.55
                ),
                color="#2B8277"
            )

            group.add(fiber)

        return group

    # ==============================================================
    # ORGANIC PEACOCK EYE
    # ==============================================================

    def make_eye(self):

        center = np.array([
            0.0,
            1.05,
            0
        ])

        eye = VGroup()

        # ----------------------------------------------------------
        # Outer green structure
        # ----------------------------------------------------------

        outer = self.irregular_ellipse(
            center,
            1.48,
            1.78,
            0.12,
            "#075A50",
            0.78
        )

        eye.add(outer)

        # ----------------------------------------------------------
        # Emerald transition
        # ----------------------------------------------------------

        emerald = self.irregular_ellipse(
            center + UP * 0.02,
            1.22,
            1.50,
            0.10,
            "#397A43",
            0.92
        )

        eye.add(emerald)

        # ----------------------------------------------------------
        # Golden / bronze region
        # ----------------------------------------------------------

        gold = self.irregular_ellipse(
            center + UP * 0.015,
            0.95,
            1.22,
            0.08,
            "#A97924",
            0.96
        )

        eye.add(gold)

        # ----------------------------------------------------------
        # Turquoise region
        # ----------------------------------------------------------

        turquoise = self.irregular_ellipse(
            center + UP * 0.01,
            0.74,
            0.96,
            0.06,
            "#087D8A",
            1
        )

        eye.add(turquoise)

        # ----------------------------------------------------------
        # Krishna-blue center
        # ----------------------------------------------------------

        blue = self.irregular_ellipse(
            center + UP * 0.01,
            0.48,
            0.70,
            0.05,
            "#17479D",
            1
        )

        eye.add(blue)

        # ----------------------------------------------------------
        # Dark pupil
        # ----------------------------------------------------------

        pupil = self.irregular_ellipse(
            center + UP * 0.015,
            0.24,
            0.43,
            0.035,
            "#04061B",
            1
        )

        eye.add(pupil)

        # ----------------------------------------------------------
        # Tiny natural highlight
        # ----------------------------------------------------------

        highlight = Dot(
            center + np.array([
                -0.10,
                0.27,
                0
            ]),
            radius=0.045,
            color="#D7FFFF"
        )

        eye.add(highlight)

        return eye

    # ==============================================================
    # IRREGULAR ELLIPSE
    # ==============================================================

    def irregular_ellipse(
        self,
        center,
        rx,
        ry,
        irregularity,
        fill,
        opacity
    ):

        # Fixed random shape
        phase = np.random.uniform(
            0,
            TAU
        )

        def shape(t):

            r = (
                1
                + irregularity
                * 0.15
                * np.sin(5 * t + phase)
                + irregularity
                * 0.08
                * np.sin(9 * t)
            )

            return center + np.array([
                rx * r * np.cos(t),
                ry * r * np.sin(t),
                0
            ])

        obj = ParametricFunction(
            shape,
            t_range=[0, TAU],
            stroke_width=1.2,
            stroke_color=fill,
            fill_color=fill,
            fill_opacity=opacity
        )

        return obj


    
    # =========================================================
    #  PREPARE TITLE
    # =========================================================
    
    happy = Text(
        "HAPPY",
        font="DejaVu Sans",
            weight=BOLD
        ).scale(0.95)
    
    janmashtami = Text(
            "JANMASHTAMI",
            font="DejaVu Sans",
            weight=BOLD
        ).scale(0.62)
    
    happy.move_to(UP * 0.35)
    janmashtami.next_to(
            happy,
            DOWN,
            buff=0.15
        )
    
    happy.set_color_by_gradient(
            "#55E8FF",
            "#297373"
        )
    
    janmashtami.set_color_by_gradient(
            "#92711F",
            "#55E8E0",
            "#216260"
        )
    
    title = VGroup(
            happy,
            janmashtami
        )
    

    # ==============================================================
    # COSMIC PARTICLES
    # ==============================================================

    def make_particles(self):

        particles = VGroup()

        for _ in range(130):

            angle = np.random.uniform(
                0,
                TAU
            )

            radius = np.random.uniform(
                2.4,
                4.7
            )

            x = radius * np.cos(angle)
            y = (
                0.8
                + radius * np.sin(angle)
            )

            particle = Dot(
                [x, y, 0],
                radius=np.random.uniform(
                    0.005,
                    0.020
                ),
                color=np.random.choice([
                    "#83EAF2",
                    "#B7F8FF",
                    "#6ED6E2"
                ])
            )

            particle.set_opacity(
                np.random.uniform(
                    0.25,
                    0.75
                )
            )

            particles.add(particle)

        return particles

        