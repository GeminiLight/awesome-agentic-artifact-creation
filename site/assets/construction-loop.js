const root = document.querySelector("[data-construction-loop]");
const THREE_MODULE_URL =
  "https://cdn.jsdelivr.net/npm/three@0.185.1/build/three.module.min.js";

if (root) {
  const viewport = root.querySelector(".loop-viewport");
  const motionToggle = root.querySelector("[data-loop-motion]");
  const progressLabel = root.querySelector("[data-loop-progress]");
  const statusText = root.querySelector("[data-loop-status]");
  const defaultStatusText = statusText?.textContent || "";
  const labelElements = new Map(
    [...root.querySelectorAll("[data-loop-label]")].map((label) => [
      label.dataset.loopLabel,
      label,
    ]),
  );
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const narrowViewport = window.matchMedia("(max-width: 719px)");
  const mobileProcess = setupMobileProcess();
  let threeLoadStarted = false;
  let threeNearViewportObserver = null;

  function requestThreeModule() {
    if (threeLoadStarted) return;
    threeLoadStarted = true;
    import(THREE_MODULE_URL)
      .then((THREE) => initializeConstructionLoop(THREE))
      .catch((error) => {
        console.error("Construction process could not initialize", error);
        root.classList.remove("is-loading", "is-ready");
        root.classList.add("is-fallback");
        motionToggle.hidden = true;
      });
  }

  function constructionLoopIsNearViewport() {
    const bounds = root.getBoundingClientRect();
    return bounds.bottom >= -160 && bounds.top <= window.innerHeight + 160;
  }

  function loadThreeWhenNearViewport() {
    if (threeLoadStarted || narrowViewport.matches) return;
    if (constructionLoopIsNearViewport()) {
      requestThreeModule();
      return;
    }
    if (!("IntersectionObserver" in window)) {
      requestThreeModule();
      return;
    }
    threeNearViewportObserver?.disconnect();
    threeNearViewportObserver = new IntersectionObserver(
      (entries, observer) => {
        if (!entries.some((entry) => entry.isIntersecting)) return;
        observer.disconnect();
        requestThreeModule();
      },
      { rootMargin: "160px 0px" },
    );
    threeNearViewportObserver.observe(root);
  }

  function activateResponsiveExperience() {
    if (narrowViewport.matches) {
      root.classList.add("is-mobile-process");
      root.classList.remove("is-loading", "is-fallback");
      motionToggle.hidden = true;
      threeNearViewportObserver?.disconnect();
      mobileProcess.start();
      return;
    }

    root.classList.remove("is-mobile-process");
    mobileProcess.stop();
    statusText.textContent = defaultStatusText;
    if (reducedMotion.matches || !window.WebGLRenderingContext) {
      root.classList.remove("is-loading", "is-ready");
      root.classList.add("is-fallback");
      motionToggle.hidden = true;
      return;
    }
    root.classList.remove("is-fallback");
    if (!root.classList.contains("is-ready")) {
      root.classList.add("is-loading");
    }
    motionToggle.hidden = false;
    loadThreeWhenNearViewport();
  }

  function setupMobileProcess() {
    const steps = [...root.querySelectorAll("[data-loop-mobile-step]")];
    const stages = steps.map((step) => step.dataset.loopMobileStep);
    const stageCopy = {
      task: "Define the goal, constraints, and acceptance criteria.",
      policy: "Choose the decision control and agent topology.",
      representation: "Construct through an editable intermediate form.",
      verification: "Observe the result and return actionable feedback.",
      artifact: "Release the accepted artifact into the next task cycle.",
    };
    let currentIndex = 0;
    let timer = 0;
    let processIsVisible = !("IntersectionObserver" in window);

    function showStage(index) {
      currentIndex = (index + steps.length) % steps.length;
      const currentStage = stages[currentIndex];
      steps.forEach((step, stepIndex) => {
        const active = stepIndex === currentIndex;
        step.classList.toggle("is-active", active);
        step.setAttribute("aria-pressed", String(active));
      });
      root.dataset.mobileStage = currentStage;
      if (narrowViewport.matches) {
        statusText.textContent = stageCopy[currentStage];
      }
    }

    function schedule() {
      window.clearTimeout(timer);
      if (
        reducedMotion.matches ||
        !narrowViewport.matches ||
        !processIsVisible ||
        document.hidden
      ) {
        return;
      }
      timer = window.setTimeout(() => {
        showStage(currentIndex + 1);
        schedule();
      }, 3400);
    }

    steps.forEach((step, index) => {
      step.addEventListener("click", () => {
        showStage(index);
        schedule();
      });
    });

    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(
        ([entry]) => {
          processIsVisible = entry.isIntersecting;
          schedule();
        },
        { threshold: 0.2 },
      );
      observer.observe(root);
    }
    document.addEventListener("visibilitychange", schedule);
    showStage(0);

    return {
      start: schedule,
      stop() {
        window.clearTimeout(timer);
      },
    };
  }

  activateResponsiveExperience();
  narrowViewport.addEventListener("change", activateResponsiveExperience);

  function initializeConstructionLoop(THREE) {
    const colors = {
      ink: 0x172033,
      navy: 0x133782,
      coral: 0xf45f49,
      coralLight: 0xffb09f,
      lavender: 0x9568d7,
      lavenderLight: 0xd9c5f5,
      blue: 0x4d9ae7,
      blueDark: 0x176ac2,
      blueLight: 0xb9dcf8,
      teal: 0x55c7c5,
      tealLight: 0xbcebea,
      deepTeal: 0x11969a,
      surface: 0xf0f3f6,
      line: 0xd5dee8,
      white: 0xffffff,
    };
    const stageColors = {
      task: colors.coral,
      policy: colors.lavender,
      representation: colors.blueDark,
      verification: colors.deepTeal,
      artifact: colors.deepTeal,
    };
    const stageDetails = {
      task: "Goal, constraints, and acceptance criteria",
      policy: "Decision control and agent topology",
      representation: "Intermediate form and edit interface",
      verification: "Observation source and feedback function",
      artifact: "Release the accepted artifact",
    };
    const flowDetails = [
      { label: "Task specification", stage: "task" },
      { label: "Construction policy", stage: "policy" },
      { label: "Operational representation", stage: "representation" },
      { label: "Runtime verification", stage: "verification" },
      { label: "Delivered artifact", stage: "artifact" },
    ];
    const STAGE_DURATION_SECONDS = 3.4;
    const ACTIVE_MOTION_TEMPO = 0.62;

    const renderer = new THREE.WebGLRenderer({
      alpha: true,
      antialias: true,
      powerPreference: "high-performance",
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.75));
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 0.93;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.VSMShadowMap;
    renderer.domElement.setAttribute("aria-hidden", "true");
    viewport.prepend(renderer.domElement);

    const scene = new THREE.Scene();
    const camera = new THREE.OrthographicCamera(-9.2, 9.2, 4, -4, 0.1, 80);
    camera.position.set(0, 7.55, 15.8);
    camera.lookAt(0, 0.72, 0.15);

    const world = new THREE.Group();
    world.position.y = -0.14;
    world.scale.set(1, 1.08, 1.23);
    scene.add(world);

    scene.add(new THREE.HemisphereLight(0xfafcff, 0xb8c8d4, 1.18));
    const keyLight = new THREE.DirectionalLight(0xfffdf9, 2.68);
    keyLight.position.set(-3, 11, 8);
    keyLight.castShadow = true;
    keyLight.shadow.mapSize.set(2048, 2048);
    keyLight.shadow.camera.left = -12;
    keyLight.shadow.camera.right = 12;
    keyLight.shadow.camera.top = 8;
    keyLight.shadow.camera.bottom = -8;
    keyLight.shadow.bias = -0.0008;
    keyLight.shadow.radius = 3.2;
    keyLight.shadow.blurSamples = 8;
    scene.add(keyLight);
    const fillLight = new THREE.DirectionalLight(0xa7ddda, 0.44);
    fillLight.position.set(7, 5, 3);
    scene.add(fillLight);
    const rimLight = new THREE.DirectionalLight(0xb8d7ff, 0.5);
    rimLight.position.set(2, 7, -7);
    scene.add(rimLight);

    const ground = new THREE.Mesh(
      new THREE.PlaneGeometry(22, 10),
      new THREE.ShadowMaterial({ color: 0x274660, opacity: 0.2 }),
    );
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = -0.29;
    ground.receiveShadow = true;
    world.add(ground);

    const stageGroups = new Map();
    const stageMeshes = new Map();
    const stageAccents = new Map();
    const stageMotionState = {
      task: { card: null, targetRing: null, checks: [], bars: [] },
      policy: { nodes: [], controls: [] },
      representation: { layers: [], blueprint: null, modes: [] },
      verification: { arch: null, dialRim: null, needle: null, specimens: [] },
      artifact: { cube: null, pieces: [], star: null },
    };
    Object.keys(stageColors).forEach((stage) => {
      const group = new THREE.Group();
      group.userData.baseY = 0;
      group.userData.hoverAmount = 0;
      group.userData.activeAmount = 0;
      group.userData.active = false;
      group.userData.hovered = false;
      stageGroups.set(stage, group);
      stageMeshes.set(stage, []);
      world.add(group);
    });

    function material(color, options = {}) {
      return new THREE.MeshPhysicalMaterial({
        color,
        roughness: options.roughness ?? 0.48,
        metalness: options.metalness ?? 0.04,
        clearcoat: options.clearcoat ?? 0.16,
        clearcoatRoughness: options.clearcoatRoughness ?? 0.42,
        ior: options.ior ?? 1.46,
        specularIntensity: options.specularIntensity ?? 0.46,
        transparent: options.transparent ?? false,
        opacity: options.opacity ?? 1,
        depthWrite: options.depthWrite ?? true,
      });
    }

    function roundedShape(width, depth, radius) {
      const x = -width / 2;
      const y = -depth / 2;
      const shape = new THREE.Shape();
      shape.moveTo(x + radius, y);
      shape.lineTo(x + width - radius, y);
      shape.quadraticCurveTo(x + width, y, x + width, y + radius);
      shape.lineTo(x + width, y + depth - radius);
      shape.quadraticCurveTo(x + width, y + depth, x + width - radius, y + depth);
      shape.lineTo(x + radius, y + depth);
      shape.quadraticCurveTo(x, y + depth, x, y + depth - radius);
      shape.lineTo(x, y + radius);
      shape.quadraticCurveTo(x, y, x + radius, y);
      return shape;
    }

    function roundedSlab(width, depth, height, radius, color, options = {}) {
      const geometry = new THREE.ExtrudeGeometry(roundedShape(width, depth, radius), {
        depth: height,
        bevelEnabled: true,
        bevelSegments: options.bevelSegments ?? 3,
        bevelSize: options.bevelSize ?? Math.min(radius * 0.28, 0.07),
        bevelThickness: options.bevelThickness ?? 0.055,
        curveSegments: 8,
        steps: 1,
      });
      geometry.center();
      geometry.rotateX(-Math.PI / 2);
      const mesh = new THREE.Mesh(geometry, material(color, options));
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      return mesh;
    }

    function box(width, height, depth, color, options = {}) {
      const mesh = new THREE.Mesh(
        new THREE.BoxGeometry(width, height, depth),
        material(color, options),
      );
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      return mesh;
    }

    function cylinder(radius, height, color, segments = 32, options = {}) {
      const mesh = new THREE.Mesh(
        new THREE.CylinderGeometry(radius, radius, height, segments),
        material(color, options),
      );
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      return mesh;
    }

    function curveThrough(points, tension = 0.45) {
      return new THREE.CatmullRomCurve3(
        points.map((point) => new THREE.Vector3(...point)),
        false,
        "catmullrom",
        tension,
      );
    }

    function tube(curve, radius, color, options = {}) {
      const mesh = new THREE.Mesh(
        new THREE.TubeGeometry(curve, options.segments ?? 48, radius, 10, false),
        material(color, {
          roughness: options.roughness ?? 0.4,
          metalness: options.metalness ?? 0.06,
          transparent: options.transparent,
          opacity: options.opacity,
          depthWrite: options.depthWrite,
        }),
      );
      mesh.castShadow = true;
      return mesh;
    }

    function arrowAt(curve, color, scale = 1) {
      const point = curve.getPointAt(0.98);
      const tangent = curve.getTangentAt(0.98).normalize();
      const arrow = new THREE.Mesh(
        new THREE.ConeGeometry(0.14 * scale, 0.34 * scale, 20),
        material(color, { roughness: 0.35 }),
      );
      arrow.position.copy(point);
      arrow.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), tangent);
      arrow.castShadow = true;
      return arrow;
    }

    function registerStage(stage, object) {
      object.traverse((child) => {
        if (!child.isMesh) return;
        child.userData.stage = stage;
        stageMeshes.get(stage).push(child);
      });
      stageGroups.get(stage).add(object);
    }

    function addActivationHalo(stage, host, radius, depthScale = 1) {
      const halo = new THREE.Group();
      halo.position.y = 0.28;
      const rings = [
        { radius, tube: 0.035, opacity: 0.76 },
        { radius: radius * 0.78, tube: 0.018, opacity: 0.48 },
      ].map((ringConfig, index) => {
        const ring = new THREE.Mesh(
          new THREE.TorusGeometry(ringConfig.radius, ringConfig.tube, 10, 72),
          new THREE.MeshBasicMaterial({
            color: stageColors[stage],
            transparent: true,
            opacity: 0,
            depthWrite: false,
            blending: THREE.AdditiveBlending,
          }),
        );
        ring.rotation.x = -Math.PI / 2;
        ring.scale.y = depthScale;
        ring.renderOrder = 3;
        ring.userData.baseDepthScale = depthScale;
        ring.userData.maxOpacity = ringConfig.opacity;
        ring.userData.phase = index * Math.PI;
        halo.add(ring);
        return ring;
      });
      host.add(halo);
      stageAccents.set(stage, { halo, rings });
    }

    const centralPlatform = roundedSlab(10.95, 3.48, 0.38, 0.42, colors.white, {
      roughness: 0.62,
      bevelSize: 0.1,
      bevelThickness: 0.08,
    });
    centralPlatform.position.set(-0.25, 0.02, 0.08);
    world.add(centralPlatform);

    const platformInset = roundedSlab(10.5, 3.06, 0.055, 0.34, 0xeaf0f4, {
      roughness: 0.72,
      clearcoat: 0.06,
      bevelSize: 0.025,
      bevelThickness: 0.02,
    });
    platformInset.position.set(-0.25, 0.235, 0.08);
    world.add(platformInset);

    [
      [-5.23, -1.3],
      [4.73, -1.3],
      [-5.23, 1.46],
      [4.73, 1.46],
    ].forEach(([x, z]) => {
      const fastener = cylinder(0.045, 0.025, 0x9aabb9, 24, {
        roughness: 0.3,
        metalness: 0.46,
        clearcoat: 0.24,
      });
      fastener.position.set(x, 0.29, z);
      world.add(fastener);
    });

    const platformFrontContour = curveThrough(
      [
        [-5.42, 0.2, 1.57],
        [-4.72, 0.2, 1.76],
        [-2.9, 0.2, 1.76],
        [-2.42, 0.17, 1.6],
        [-1.94, 0.2, 1.76],
        [1.14, 0.2, 1.76],
        [1.62, 0.17, 1.6],
        [2.1, 0.2, 1.76],
        [5.16, 0.2, 1.66],
      ],
      0.22,
    );
    world.add(
      tube(platformFrontContour, 0.028, 0xd9e1e8, {
        segments: 88,
        roughness: 0.5,
      }),
    );

    function addFeedbackPort(x, outerColor) {
      const port = new THREE.Group();
      const collar = roundedSlab(0.7, 0.48, 0.18, 0.1, outerColor, {
        roughness: 0.38,
        clearcoat: 0.34,
      });
      collar.position.set(0, 0.44, 1.55);
      port.add(collar);
      const face = roundedSlab(0.56, 0.6, 0.18, 0.1, outerColor, {
        roughness: 0.36,
        clearcoat: 0.36,
      });
      face.rotation.x = Math.PI / 2;
      face.position.set(0, 0.37, 1.74);
      port.add(face);
      const socket = roundedSlab(0.3, 0.34, 0.09, 0.065, 0x08767d, {
        roughness: 0.28,
        clearcoat: 0.4,
      });
      socket.rotation.x = Math.PI / 2;
      socket.position.set(0, 0.34, 1.86);
      port.add(socket);
      port.position.x = x;
      world.add(port);
    }
    addFeedbackPort(-4.1, colors.lavender);
    addFeedbackPort(4.12, colors.teal);

    const frameLeft = curveThrough(
      [
        [-5.62, 0.48, -1.58],
        [-5.62, 2.78, -1.58],
        [-5.38, 3.08, -1.58],
        [-3.4, 3.1, -1.58],
        [-1.05, 3.1, -1.58],
      ],
      0.18,
    );
    const frameRight = curveThrough(
      [
        [1.05, 3.1, -1.58],
        [3.35, 3.1, -1.58],
        [5.12, 3.08, -1.58],
        [5.35, 2.78, -1.58],
        [5.35, 0.48, -1.58],
      ],
      0.18,
    );
    world.add(
      tube(frameLeft, 0.045, colors.blueDark, { segments: 72 }),
      tube(frameRight, 0.045, colors.blueDark, { segments: 72 }),
    );
    [
      [-1.05, 3.1, -1.58],
      [1.05, 3.1, -1.58],
      [-5.62, 0.48, -1.58],
      [5.35, 0.48, -1.58],
    ].forEach(([x, y, z]) => {
      const cap = new THREE.Mesh(
        new THREE.SphereGeometry(0.067, 18, 12),
        material(colors.blueDark, { roughness: 0.3, clearcoat: 0.3 }),
      );
      cap.position.set(x, y, z);
      cap.castShadow = true;
      world.add(cap);
    });

    function addTaskStage() {
      const group = new THREE.Group();
      group.position.set(-7.18, 0, 0.15);

      const pedestal = roundedSlab(2.05, 2.35, 0.32, 0.2, colors.white, {
        roughness: 0.62,
      });
      pedestal.position.y = 0.02;
      group.add(pedestal);

      const card = roundedSlab(1.84, 2.45, 0.22, 0.18, colors.coral, {
        roughness: 0.46,
        bevelSize: 0.08,
      });
      card.rotation.x = Math.PI / 2;
      card.position.set(0, 1.32, 0.05);
      group.add(card);
      stageMotionState.task.card = card;

      const cardInset = roundedSlab(1.58, 2.18, 0.08, 0.13, 0xfff8f6, {
        roughness: 0.78,
        bevelSize: 0.035,
        bevelThickness: 0.025,
      });
      cardInset.rotation.x = Math.PI / 2;
      cardInset.position.set(0, 1.32, 0.19);
      group.add(cardInset);

      const targetRing = new THREE.Mesh(
        new THREE.TorusGeometry(0.2, 0.028, 10, 36),
        material(colors.coral, { roughness: 0.34 }),
      );
      targetRing.position.set(0, 2.04, 0.27);
      targetRing.castShadow = true;
      group.add(targetRing);
      stageMotionState.task.targetRing = targetRing;
      const targetDot = cylinder(0.045, 0.06, colors.coral, 24);
      targetDot.rotation.x = Math.PI / 2;
      targetDot.position.set(0, 2.04, 0.28);
      group.add(targetDot);
      [0, Math.PI / 2].forEach((rotation) => {
        const cross = box(0.53, 0.025, 0.025, colors.coral);
        cross.rotation.z = rotation;
        cross.position.set(0, 2.04, 0.28);
        group.add(cross);
      });

      [0.72, 0.45, 0.18].forEach((y, index) => {
        const tick = box(0.14, 0.14, 0.025, colors.coralLight);
        tick.position.set(-0.52, y, 0.27);
        group.add(tick);
        const check = tube(
          curveThrough(
            [
              [-0.57, y, 0.3],
              [-0.53, y - 0.045, 0.3],
              [-0.45, y + 0.065, 0.3],
            ],
            0.12,
          ),
          0.013,
          colors.coral,
          { segments: 12 },
        );
        group.add(check);
        check.userData.baseZ = check.position.z;
        stageMotionState.task.checks.push(check);
        const line = box(index === 2 ? 0.56 : 0.7, 0.035, 0.025, colors.coral);
        line.position.set(-0.03, y, 0.27);
        group.add(line);
      });

      const miniBars = [0.13, 0.23, 0.34, 0.46, 0.58];
      miniBars.forEach((height, index) => {
        const bar = box(0.055, height, 0.03, colors.coral);
        bar.position.set(0.36 + index * 0.1, 0.25 + height / 2, 0.28);
        group.add(bar);
        stageMotionState.task.bars.push(bar);
      });
      group.add(
        tube(
          curveThrough(
            [
              [0.34, 0.36, 0.31],
              [0.45, 0.49, 0.31],
              [0.54, 0.43, 0.31],
              [0.66, 0.62, 0.31],
              [0.77, 0.76, 0.31],
            ],
            0.18,
          ),
          0.016,
          colors.coral,
          { segments: 20 },
        ),
      );
      addActivationHalo("task", group, 1.12, 0.82);
      registerStage("task", group);
    }

    function addPolicyStage() {
      const group = new THREE.Group();
      group.position.set(-4.12, 0, 0.08);
      const base = roundedSlab(2.72, 2.86, 0.28, 0.22, colors.lavenderLight, {
        roughness: 0.54,
      });
      base.position.y = 0.34;
      group.add(base);
      const insetSurface = roundedSlab(2.48, 2.62, 0.045, 0.18, 0xeadff8, {
        roughness: 0.56,
        clearcoat: 0.12,
        bevelSize: 0.025,
        bevelThickness: 0.02,
      });
      insetSurface.position.y = 0.51;
      group.add(insetSurface);

      const nodes = [
        [-0.78, -0.72],
        [0.66, -0.65],
        [-0.84, 0.08],
        [0.28, 0.18],
        [-0.38, 0.92],
        [0.84, 0.91],
      ];
      const connections = [
        [0, 1],
        [0, 2],
        [2, 3],
        [2, 4],
        [3, 5],
      ];
      connections.forEach(([start, end]) => {
        const [x1, z1] = nodes[start];
        const [x2, z2] = nodes[end];
        const curve = curveThrough([
          [x1, 0.64, z1],
          [(x1 + x2) / 2, 0.67, (z1 + z2) / 2],
          [x2, 0.64, z2],
        ]);
        group.add(tube(curve, 0.07, colors.white, { segments: 24 }));
      });
      nodes.forEach(([x, z], index) => {
        const pad = cylinder(index > 3 ? 0.18 : 0.24, 0.18, colors.white);
        pad.position.set(x, 0.62, z);
        group.add(pad);
        const node = cylinder(index > 3 ? 0.16 : 0.21, 0.2, colors.lavender);
        node.position.set(x, 0.78, z);
        group.add(node);
        node.userData.baseY = node.position.y;
        node.userData.motionIndex = index;
        stageMotionState.policy.nodes.push(node);
      });

      const controls = roundedSlab(1.08, 0.52, 0.16, 0.09, 0xeadcf9);
      controls.position.set(-0.64, 0.66, 1.04);
      group.add(controls);
      const decisionPad = roundedSlab(1.02, 0.52, 0.16, 0.09, 0xe4d3f7);
      decisionPad.position.set(0.72, 0.66, 1.04);
      group.add(decisionPad);

      const policyControlLayout = [
        { kind: "box", x: -0.88, z: 1.04 },
        { kind: "cylinder", x: -0.48, z: 1.04 },
        { kind: "cylinder", x: 0.48, z: 0.98 },
        { kind: "cylinder", x: 0.74, z: 1.12 },
        { kind: "cylinder", x: 1, z: 0.98 },
      ];
      policyControlLayout.forEach(({ kind, x, z }) => {
        const control = kind === "box"
          ? box(0.18, 0.13, 0.18, colors.lavender)
          : cylinder(0.09, 0.13, colors.lavender);
        control.position.set(x, 0.83, z);
        group.add(control);
        control.userData.baseY = control.position.y;
        stageMotionState.policy.controls.push(control);
      });
      addActivationHalo("policy", group, 1.48, 0.94);
      registerStage("policy", group);
    }

    function addRepresentationStage() {
      const group = new THREE.Group();
      group.position.set(-0.36, 0, 0.04);
      [0, 1, 2, 3].forEach((index) => {
        const layer = roundedSlab(
          3.6 - index * 0.09,
          3.04 - index * 0.08,
          0.15,
          0.21,
          index === 3 ? colors.blueLight : index === 0 ? 0x6fb0ee : colors.blue,
          { roughness: 0.49 },
        );
        layer.position.set(index * 0.055, 0.35 + index * 0.13, -index * 0.04);
        group.add(layer);
        layer.userData.basePosition = layer.position.clone();
        layer.userData.motionIndex = index;
        stageMotionState.representation.layers.push(layer);
      });

      const blueprint = roundedSlab(1.68, 1.76, 0.09, 0.1, 0xdceeff, {
        roughness: 0.58,
      });
      blueprint.position.set(-0.42, 0.96, -0.13);
      group.add(blueprint);
      stageMotionState.representation.blueprint = blueprint;
      [-0.78, -0.42, -0.06, 0.3].forEach((x) => {
        const gridLine = box(0.016, 0.025, 1.45, 0x86bdf0);
        gridLine.position.set(x, 1.04, -0.13);
        group.add(gridLine);
      });
      [-0.66, -0.3, 0.06, 0.42].forEach((z) => {
        const gridLine = box(1.4, 0.025, 0.016, 0x86bdf0);
        gridLine.position.set(-0.42, 1.04, z);
        group.add(gridLine);
      });

      const nodePositions = [
        [-0.98, -0.6],
        [-0.2, -0.1],
        [-0.92, 0.56],
        [0.18, 0.65],
      ];
      nodePositions.forEach(([x, z], index) => {
        const node = index % 2
          ? roundedSlab(0.35, 0.35, 0.28, 0.07, colors.white)
          : cylinder(0.17, 0.22, colors.blueDark);
        node.position.set(x, 1.16 + index * 0.015, z);
        group.add(node);
      });
      [[-0.98, -0.6, -0.2, -0.1], [-0.2, -0.1, 0.18, 0.65]].forEach(([x1, z1, x2, z2]) => {
        group.add(
          tube(
            curveThrough([[x1, 1.2, z1], [(x1 + x2) / 2, 1.25, (z1 + z2) / 2], [x2, 1.2, z2]]),
            0.035,
            colors.blueDark,
            { segments: 24 },
          ),
        );
      });

      const editPanel = roundedSlab(0.78, 1.1, 0.18, 0.1, colors.white, {
        roughness: 0.6,
      });
      editPanel.position.set(0.92, 1.06, 0.28);
      group.add(editPanel);
      [-0.07, 0.18, 0.43].forEach((z) => {
        const line = box(0.42, 0.025, 0.025, colors.blueDark);
        line.position.set(0.92, 1.18, z);
        group.add(line);
      });
      [0, 1, 2].forEach((index) => {
        const disc = cylinder(0.23, 0.15, index === 2 ? 0x0e61b6 : colors.blueDark);
        disc.position.set(0.72, 1.04 + index * 0.15, -0.86);
        group.add(disc);
      });

      const chartPanel = roundedSlab(0.82, 0.62, 0.13, 0.08, colors.white, {
        roughness: 0.58,
        clearcoat: 0.12,
      });
      chartPanel.position.set(-1.15, 1.02, 0.98);
      group.add(chartPanel);
      const chartAxisX = box(0.57, 0.025, 0.022, 0x85b8e9);
      chartAxisX.position.set(-1.13, 1.11, 1.15);
      group.add(chartAxisX);
      const chartAxisZ = box(0.022, 0.025, 0.38, 0x85b8e9);
      chartAxisZ.position.set(-1.4, 1.11, 0.99);
      group.add(chartAxisZ);
      group.add(
        tube(
          curveThrough(
            [
              [-1.35, 1.14, 1.08],
              [-1.24, 1.14, 0.99],
              [-1.1, 1.14, 1.04],
              [-0.96, 1.14, 0.86],
              [-0.85, 1.14, 0.79],
            ],
            0.2,
          ),
          0.018,
          colors.blueDark,
          { segments: 22 },
        ),
      );

      const modePanel = roundedSlab(0.66, 0.62, 0.13, 0.08, 0xd8ebfc, {
        roughness: 0.54,
      });
      modePanel.position.set(1.18, 0.96, 0.92);
      group.add(modePanel);
      [-0.17, 0, 0.17].forEach((offset, index) => {
        const mode = index === 1
          ? cylinder(0.075, 0.12, colors.blueDark)
          : roundedSlab(0.14, 0.14, 0.11, 0.03, colors.white);
        mode.position.set(1.18 + offset, 1.09, 0.92);
        group.add(mode);
        mode.userData.baseY = mode.position.y;
        mode.userData.motionIndex = index;
        stageMotionState.representation.modes.push(mode);
      });
      addActivationHalo("representation", group, 1.82, 0.84);
      registerStage("representation", group);
    }

    let verificationNeedle;
    function addVerificationStage() {
      const group = new THREE.Group();
      group.position.set(3.52, 0, 0.08);
      const base = roundedSlab(2.8, 2.96, 0.29, 0.22, colors.tealLight, {
        roughness: 0.51,
      });
      base.position.y = 0.34;
      group.add(base);
      const insetSurface = roundedSlab(2.56, 2.7, 0.045, 0.18, 0xdaf5f2, {
        roughness: 0.54,
        clearcoat: 0.12,
        bevelSize: 0.025,
        bevelThickness: 0.02,
      });
      insetSurface.position.y = 0.51;
      group.add(insetSurface);

      const arch = new THREE.Mesh(
        new THREE.TorusGeometry(0.78, 0.14, 16, 52, Math.PI),
        material(colors.teal, { roughness: 0.42 }),
      );
      arch.position.set(-0.14, 1.26, 0.04);
      arch.castShadow = true;
      group.add(arch);
      stageMotionState.verification.arch = arch;
      [-0.92, 0.64].forEach((x) => {
        const support = box(0.29, 0.7, 0.31, colors.teal);
        support.position.set(x, 0.92, 0.04);
        group.add(support);
        const foot = roundedSlab(0.42, 0.46, 0.2, 0.07, colors.white);
        foot.position.set(x, 0.6, 0.04);
        group.add(foot);
      });

      const dial = cylinder(0.5, 0.13, colors.white, 40);
      dial.rotation.x = Math.PI / 2;
      dial.position.set(-0.14, 1.17, 0.53);
      group.add(dial);
      const dialRim = new THREE.Mesh(
        new THREE.TorusGeometry(0.49, 0.035, 10, 48),
        material(colors.teal, {
          roughness: 0.34,
          clearcoat: 0.36,
        }),
      );
      dialRim.position.set(-0.14, 1.17, 0.61);
      dialRim.castShadow = true;
      group.add(dialRim);
      stageMotionState.verification.dialRim = dialRim;
      for (let index = 0; index < 12; index += 1) {
        const angle = (index / 12) * Math.PI * 2;
        const tick = box(0.025, 0.11, 0.025, colors.deepTeal);
        tick.position.set(
          -0.14 + Math.sin(angle) * 0.38,
          1.17 + Math.cos(angle) * 0.38,
          0.61,
        );
        tick.rotation.z = -angle;
        group.add(tick);
      }
      verificationNeedle = new THREE.Group();
      verificationNeedle.position.set(-0.14, 1.17, 0.64);
      const needleShape = new THREE.Shape();
      needleShape.moveTo(-0.08, -0.065);
      needleShape.lineTo(0.44, 0);
      needleShape.lineTo(-0.08, 0.065);
      needleShape.closePath();
      const needle = new THREE.Mesh(
        new THREE.ExtrudeGeometry(needleShape, {
          depth: 0.035,
          bevelEnabled: true,
          bevelSegments: 2,
          bevelSize: 0.012,
          bevelThickness: 0.01,
        }),
        material(colors.deepTeal, {
          roughness: 0.28,
          clearcoat: 0.42,
        }),
      );
      needle.castShadow = true;
      verificationNeedle.add(needle);
      const needleHub = cylinder(0.075, 0.06, colors.deepTeal, 24);
      needleHub.rotation.x = Math.PI / 2;
      verificationNeedle.add(needleHub);
      group.add(verificationNeedle);
      stageMotionState.verification.needle = verificationNeedle;

      const ruler = roundedSlab(0.3, 1.48, 0.1, 0.06, colors.white);
      ruler.rotation.x = Math.PI / 2;
      ruler.position.set(0.97, 1.09, 0.38);
      group.add(ruler);
      for (let index = 0; index < 8; index += 1) {
        const mark = box(index % 2 ? 0.11 : 0.17, 0.02, 0.025, colors.deepTeal);
        mark.position.set(0.97, 0.57 + index * 0.15, 0.47);
        group.add(mark);
      }

      [-0.78, 0, 0.78].forEach((x, index) => {
        const columnBase = cylinder(0.26, 0.13, colors.deepTeal);
        columnBase.position.set(x, 0.46, 0.92);
        group.add(columnBase);
        [0, 1, 2].forEach((level) => {
          const cube = box(
            0.24,
            0.2,
            0.24,
            level === index ? colors.teal : 0xe6f9f7,
            { clearcoat: 0.28 },
          );
          cube.position.set(x, 0.58 + level * 0.19, 0.92);
          cube.rotation.y = Math.PI / 4;
          group.add(cube);
          cube.userData.baseY = cube.position.y;
          cube.userData.motionIndex = index * 3 + level;
          stageMotionState.verification.specimens.push(cube);
        });
        const glass = new THREE.Mesh(
          new THREE.CylinderGeometry(0.29, 0.29, 0.76, 32, 1, true),
          material(0xb9f0ed, {
            transparent: true,
            opacity: 0.17,
            roughness: 0.18,
            metalness: 0.02,
            depthWrite: false,
          }),
        );
        glass.position.set(x, 0.78, 0.92);
        group.add(glass);
        const rim = new THREE.Mesh(
          new THREE.TorusGeometry(0.29, 0.025, 8, 32),
          material(colors.deepTeal, { transparent: true, opacity: 0.58 }),
        );
        rim.rotation.x = Math.PI / 2;
        rim.position.set(x, 1.16, 0.92);
        group.add(rim);
      });
      addActivationHalo("verification", group, 1.5, 0.96);
      registerStage("verification", group);
    }

    let artifactCube;
    function addArtifactStage() {
      const group = new THREE.Group();
      group.position.set(7.02, 0, 0.08);
      const pedestal = roundedSlab(1.75, 1.72, 0.34, 0.2, colors.white, {
        roughness: 0.62,
      });
      pedestal.position.y = 0.04;
      group.add(pedestal);
      const base = roundedSlab(1.52, 1.45, 0.27, 0.18, colors.teal, {
        roughness: 0.45,
      });
      base.position.y = 0.28;
      group.add(base);

      artifactCube = new THREE.Group();
      artifactCube.position.set(0, 0.98, 0);
      artifactCube.rotation.y = -0.2;
      stageMotionState.artifact.cube = artifactCube;
      [-0.28, 0.28].forEach((x) => {
        [-0.28, 0.28].forEach((y) => {
          [-0.28, 0.28].forEach((z) => {
            const pieceTone = y > 0
              ? (x > 0 ? 0x2ba8a9 : 0x239fa2)
              : (z > 0 ? 0x158e93 : colors.deepTeal);
            const piece = roundedSlab(0.49, 0.49, 0.49, 0.065, pieceTone, {
              roughness: 0.34,
              metalness: 0.08,
              clearcoat: 0.34,
            });
            piece.position.set(x, y, z);
            piece.userData.basePosition = piece.position.clone();
            artifactCube.add(piece);
            stageMotionState.artifact.pieces.push(piece);
          });
        });
      });
      group.add(artifactCube);

      const star = new THREE.Shape();
      for (let index = 0; index < 12; index += 1) {
        const radius = index % 2 ? 0.09 : 0.18;
        const angle = (index / 12) * Math.PI * 2 - Math.PI / 2;
        const x = Math.cos(angle) * radius;
        const y = Math.sin(angle) * radius;
        if (index === 0) star.moveTo(x, y);
        else star.lineTo(x, y);
      }
      star.closePath();
      const starMesh = new THREE.Mesh(
        new THREE.ExtrudeGeometry(star, {
          depth: 0.06,
          bevelEnabled: true,
          bevelSegments: 2,
          bevelSize: 0.025,
          bevelThickness: 0.02,
        }),
        material(0x08757a, { roughness: 0.4 }),
      );
      starMesh.position.set(0, 0, 0.61);
      starMesh.castShadow = true;
      artifactCube.add(starMesh);
      stageMotionState.artifact.star = starMesh;
      addActivationHalo("artifact", group, 1.02, 0.88);
      registerStage("artifact", group);
    }

    addTaskStage();
    addPolicyStage();
    addRepresentationStage();
    addVerificationStage();
    addArtifactStage();

    function smoothPulse(phase) {
      const sine = Math.sin(phase);
      const halfWave = Math.min(1, Math.max(0, sine));
      return halfWave * halfWave * (3 - 2 * halfWave);
    }

    function animateActivationHalo(stage, elapsed, activeAmount) {
      const accent = stageAccents.get(stage);
      if (!accent) return;
      const activeMotionTime = elapsed * ACTIVE_MOTION_TEMPO;
      accent.halo.visible = activeAmount > 0.01;
      accent.halo.rotation.y = activeMotionTime * 0.22;
      accent.rings.forEach((ring, index) => {
        const pulse = 0.5 + Math.sin(activeMotionTime * 3.1 + ring.userData.phase) * 0.5;
        const expansion = 1 + activeAmount * (0.06 + pulse * 0.17 + index * 0.05);
        ring.scale.x = expansion;
        ring.scale.y = ring.userData.baseDepthScale * expansion;
        ring.material.opacity = activeAmount * ring.userData.maxOpacity * (0.58 + pulse * 0.42);
      });
    }

    function animateTaskStage(elapsed, activeAmount, hoverAmount) {
      const task = stageMotionState.task;
      const activeMotionTime = elapsed * ACTIVE_MOTION_TEMPO;
      const energy = 0.38 + activeAmount * 0.92 + hoverAmount * 0.26;
      const targetPulse = 0.5 + Math.sin(activeMotionTime * 2.7) * 0.5;
      task.targetRing.rotation.z = activeMotionTime * 0.92;
      task.targetRing.scale.setScalar(1 + targetPulse * 0.08 * energy);
      task.card.rotation.z = Math.sin(activeMotionTime * 0.82) * 0.012 + activeAmount * Math.sin(activeMotionTime * 2.5) * 0.018;

      task.checks.forEach((check, index) => {
        const scan = smoothPulse(activeMotionTime * 2.15 - index * 0.82);
        const checkScale = 1 + scan * (0.08 + activeAmount * 0.18);
        check.scale.setScalar(checkScale);
        check.position.z = check.userData.baseZ + scan * 0.04 * energy;
      });
      task.bars.forEach((bar, index) => {
        const meter = 0.5 + Math.sin(activeMotionTime * 2.45 - index * 0.52) * 0.5;
        bar.scale.y = 0.88 + meter * (0.12 + activeAmount * 0.34);
      });
    }

    function animatePolicyStage(elapsed, activeAmount, hoverAmount) {
      const policy = stageMotionState.policy;
      const activeMotionTime = elapsed * ACTIVE_MOTION_TEMPO;
      const decisionSpeed = 1.95;
      policy.nodes.forEach((node, index) => {
        const decisionWave = smoothPulse(activeMotionTime * decisionSpeed - index * 0.72);
        node.position.y = node.userData.baseY + decisionWave * (0.055 + activeAmount * 0.16);
        node.scale.setScalar(1 + decisionWave * (0.08 + activeAmount * 0.24));
      });
      policy.controls.forEach((control, index) => {
        const switchPulse = 0.5 + Math.sin(activeMotionTime * 2.8 + index * 1.35) * 0.5;
        control.position.y = control.userData.baseY + switchPulse * activeAmount * 0.06;
        control.rotation.y = Math.sin(activeMotionTime * 1.9 + index) * activeAmount * 0.3;
      });
    }

    function animateRepresentationStage(elapsed, activeAmount, hoverAmount) {
      const representation = stageMotionState.representation;
      const activeMotionTime = elapsed * ACTIVE_MOTION_TEMPO;
      const spread = activeAmount * (0.11 + (0.5 + Math.sin(activeMotionTime * 1.25) * 0.5) * 0.055);
      representation.layers.forEach((layer, index) => {
        const base = layer.userData.basePosition;
        const centeredIndex = index - (representation.layers.length - 1) / 2;
        const drift = Math.sin(activeMotionTime * 0.88 + index * 0.8);
        layer.position.x = base.x + centeredIndex * spread * 0.34;
        layer.position.y = base.y + index * spread + drift * (0.008 + hoverAmount * 0.01);
        layer.position.z = base.z - index * spread * 0.22;
        layer.rotation.y = centeredIndex * activeAmount * 0.025 + drift * 0.006;
      });
      representation.blueprint.rotation.y = Math.sin(activeMotionTime * 0.72) * 0.018 + activeAmount * 0.045;
      representation.blueprint.rotation.z = Math.sin(activeMotionTime * 1.05) * (0.006 + activeAmount * 0.016);
      representation.modes.forEach((mode, index) => {
        const selection = smoothPulse(activeMotionTime * 2.15 - index * 1.42);
        mode.position.y = mode.userData.baseY + selection * (0.025 + activeAmount * 0.09);
        mode.scale.setScalar(1 + selection * activeAmount * 0.16);
      });
    }

    function animateVerificationStage(elapsed, activeAmount, hoverAmount) {
      const verification = stageMotionState.verification;
      const activeMotionTime = elapsed * ACTIVE_MOTION_TEMPO;
      const sweepSpeed = 1.28;
      verification.needle.rotation.z = -0.5 + Math.sin(activeMotionTime * sweepSpeed) * (0.48 + activeAmount * 0.22);
      const dialPulse = 1 + (0.5 + Math.sin(activeMotionTime * 3.2) * 0.5) * activeAmount * 0.12;
      verification.dialRim.scale.setScalar(dialPulse);
      verification.arch.scale.y = 1 + Math.sin(activeMotionTime * 1.55) * (0.012 + activeAmount * 0.045);
      verification.specimens.forEach((specimen, index) => {
        const scan = smoothPulse(activeMotionTime * 2.35 - index * 0.58);
        specimen.position.y = specimen.userData.baseY + scan * activeAmount * 0.075;
        specimen.rotation.y = Math.PI / 4 + activeMotionTime * 0.15 * (index % 2 ? -1 : 1);
        specimen.scale.setScalar(1 + scan * activeAmount * 0.12);
      });
    }

    function animateArtifactStage(elapsed, activeAmount, hoverAmount) {
      const artifact = stageMotionState.artifact;
      const activeMotionTime = elapsed * ACTIVE_MOTION_TEMPO;
      const burstPulse = 0.5 + Math.sin(activeMotionTime * 2.45) * 0.5;
      const spread = 0.025 + activeAmount * (0.18 + burstPulse * 0.2) + hoverAmount * 0.05;
      artifact.cube.rotation.y = -0.2 + activeMotionTime * 0.3;
      artifact.cube.rotation.x = Math.sin(activeMotionTime * 0.78) * (0.028 + activeAmount * 0.085);
      artifact.cube.position.y = 0.98 + Math.sin(activeMotionTime * 1.1) * (0.025 + activeAmount * 0.075);
      artifact.pieces.forEach((piece, index) => {
        const base = piece.userData.basePosition;
        const stagger = 0.92 + (index % 3) * 0.06;
        piece.position.copy(base).multiplyScalar(1 + spread * stagger);
        piece.rotation.x = Math.sin(activeMotionTime * 1.7 + index) * activeAmount * 0.12;
        piece.rotation.z = Math.cos(activeMotionTime * 1.45 + index * 0.7) * activeAmount * 0.12;
      });
      const starPulse = 1 + activeAmount * (0.12 + burstPulse * 0.24);
      artifact.star.scale.setScalar(starPulse);
      artifact.star.rotation.z = -activeMotionTime * 0.62;
    }

    const stageMotionControllers = {
      task: animateTaskStage,
      policy: animatePolicyStage,
      representation: animateRepresentationStage,
      verification: animateVerificationStage,
      artifact: animateArtifactStage,
    };

    function addBridge(x, width = 1) {
      const depth = 0.58;
      const bodyEnd = width * 0.14;
      const shape = new THREE.Shape();
      shape.moveTo(-width / 2, -depth * 0.31);
      shape.lineTo(bodyEnd, -depth * 0.31);
      shape.lineTo(bodyEnd, -depth / 2);
      shape.lineTo(width / 2, 0);
      shape.lineTo(bodyEnd, depth / 2);
      shape.lineTo(bodyEnd, depth * 0.31);
      shape.lineTo(-width / 2, depth * 0.31);
      shape.closePath();
      const geometry = new THREE.ExtrudeGeometry(shape, {
        depth: 0.18,
        bevelEnabled: true,
        bevelSegments: 3,
        bevelSize: 0.04,
        bevelThickness: 0.035,
      });
      geometry.center();
      geometry.rotateX(-Math.PI / 2);
      const bridge = new THREE.Mesh(
        geometry,
        material(colors.white, {
          roughness: 0.58,
          clearcoat: 0.15,
        }),
      );
      bridge.castShadow = true;
      bridge.receiveShadow = true;
      bridge.position.set(x, 0.69, 0.07);
      world.add(bridge);
    }
    addBridge(-2.48, 0.98);
    addBridge(1.74, 0.96);
    addBridge(5.72, 1.04);

    const flows = [];
    const particleGeometry = new THREE.CapsuleGeometry(0.028, 0.1, 4, 8);
    const particleUp = new THREE.Vector3(0, 1, 0);

    function addFlow(points, color, count, speed, options = {}) {
      const curve = curveThrough(points, options.tension ?? 0.35);
      const rail = tube(curve, options.radius ?? 0.045, color, {
        segments: options.segments ?? 52,
        roughness: 0.36,
        transparent: options.transparent,
        opacity: options.opacity,
      });
      world.add(rail, arrowAt(curve, color, options.arrowScale ?? 1));
      const particles = [];
      for (let index = 0; index < count; index += 1) {
        const particle = new THREE.Mesh(
          particleGeometry,
          new THREE.MeshPhysicalMaterial({
            color,
            emissive: color,
            emissiveIntensity: 0.24,
            roughness: 0.22,
            clearcoat: 0.4,
            clearcoatRoughness: 0.25,
          }),
        );
        particle.castShadow = true;
        particles.push({ mesh: particle, offset: index / count });
        world.add(particle);
      }
      flows.push({ curve, particles, speed });
    }

    addFlow(
      [[-6.15, 0.79, 0.1], [-5.82, 0.79, 0.1], [-5.55, 0.79, 0.1]],
      colors.coral,
      4,
      0.25,
      { radius: 0.055, arrowScale: 1.05 },
    );
    addFlow(
      [[-2.88, 0.82, 0.08], [-2.48, 0.82, 0.08], [-2.08, 0.82, 0.08]],
      colors.lavender,
      4,
      0.27,
      { radius: 0.05 },
    );
    addFlow(
      [[1.4, 0.82, 0.06], [1.74, 0.82, 0.06], [2.12, 0.82, 0.06]],
      colors.blueDark,
      4,
      0.29,
      { radius: 0.05 },
    );
    addFlow(
      [[5.18, 0.82, 0.06], [5.72, 0.82, 0.06], [6.2, 0.82, 0.06]],
      colors.deepTeal,
      4,
      0.31,
      { radius: 0.055 },
    );
    const artifactToTaskFeedbackPoints = [
      [6.92, 0.52, 1.24],
      [6.55, 0.08, 2.36],
      [4.12, 0.02, 2.75],
      [0, 0, 2.92],
      [-4.2, 0.02, 2.75],
      [-6.72, 0.08, 2.35],
      [-7.1, 0.52, 1.22],
    ];
    addFlow(
      artifactToTaskFeedbackPoints,
      colors.deepTeal,
      14,
      0.12,
      { radius: 0.112, arrowScale: 1.2, segments: 112, tension: 0.16 },
    );
    const feedbackHighlight = curveThrough(
      artifactToTaskFeedbackPoints.map(([x, y, z]) => [x, y + 0.075, z - 0.018]),
      0.16,
    );
    world.add(
      tube(feedbackHighlight, 0.018, colors.tealLight, {
        segments: 112,
        roughness: 0.26,
        transparent: true,
        opacity: 0.9,
      }),
    );

    const labelAnchors = new Map();
    [
      ["loop", 0, 3.12, -1.58],
      ["task", -7.18, 1.43, 0.48],
      ["policy", -4.12, 2.53, -0.54],
      ["representation", -0.36, 2.58, -0.54],
      ["verification", 3.52, 2.53, -0.54],
      ["artifact", 7.02, 0.05, 1.18],
      ["action", -2.48, 1.08, 0.08],
      ["observation", 1.74, 1.08, 0.08],
      ["accept", 5.72, 1.08, 0.08],
      ["feedback", 0, 0.28, 2.72],
    ].forEach(([name, x, y, z]) => {
      const anchor = new THREE.Object3D();
      anchor.position.set(x, y, z);
      world.add(anchor);
      labelAnchors.set(name, anchor);
      if (stageColors[name]) {
        labelElements.get(name)?.style.setProperty(
          "--loop-stage-color",
          `#${stageColors[name].toString(16).padStart(6, "0")}`,
        );
      }
    });

    const raycaster = new THREE.Raycaster();
    const pointer = new THREE.Vector2(4, 4);
    const cameraTarget = new THREE.Vector2();
    let elapsedTime = 0;
    let previousFrameTime = performance.now();
    let hoveredStage = "";
    let manualPaused = false;
    let isVisible = true;
    let destroyed = false;

    function resize() {
      const width = Math.max(viewport.clientWidth, 1);
      const height = Math.max(viewport.clientHeight, 1);
      renderer.setSize(width, height, false);
      const aspect = width / height;
      const desiredWidth = 18.3;
      const desiredHeight = 7.7;
      let frustumWidth = desiredWidth;
      let frustumHeight = desiredWidth / aspect;
      if (frustumHeight < desiredHeight) {
        frustumHeight = desiredHeight;
        frustumWidth = desiredHeight * aspect;
      }
      camera.left = -frustumWidth / 2;
      camera.right = frustumWidth / 2;
      camera.top = frustumHeight / 2;
      camera.bottom = -frustumHeight / 2;
      camera.updateProjectionMatrix();
      renderer.render(scene, camera);
      updateLabels();
    }

    function updateLabels() {
      const width = viewport.clientWidth;
      const height = viewport.clientHeight;
      labelAnchors.forEach((anchor, name) => {
        const label = labelElements.get(name);
        if (!label) return;
        const position = anchor.getWorldPosition(new THREE.Vector3()).project(camera);
        label.style.left = `${(position.x * 0.5 + 0.5) * width}px`;
        label.style.top = `${(-position.y * 0.5 + 0.5) * height}px`;
      });
    }

    function updateHover() {
      raycaster.setFromCamera(pointer, camera);
      const hits = raycaster.intersectObjects(
        [...stageGroups.values()].flatMap((group) => group.children),
        true,
      );
      const nextStage = hits.find((hit) => hit.object.userData.stage)?.object.userData.stage || "";
      if (nextStage === hoveredStage) return;
      hoveredStage = nextStage;
      viewport.classList.toggle("has-stage-hover", Boolean(hoveredStage));
      if (hoveredStage) {
        progressLabel.textContent = stageDetails[hoveredStage];
        if (statusText) statusText.textContent = stageDetails[hoveredStage];
      } else if (statusText) {
        statusText.textContent = defaultStatusText;
      }
      statusText?.classList.toggle("is-inspecting", Boolean(hoveredStage));
    }

    function dampMotion(current, target, sharpness, delta) {
      return target + (current - target) * Math.exp(-sharpness * delta);
    }

    function updateStageEmphasis(activeStage) {
      const emphasizedStage = hoveredStage || activeStage;
      stageMeshes.forEach((meshes, stage) => {
        const emphasized = stage === emphasizedStage;
        const group = stageGroups.get(stage);
        if (group) {
          group.userData.active = emphasized;
          group.userData.hovered = stage === hoveredStage;
        }
      });
    }

    function renderFrame(elapsed, frameDelta = 1 / 60) {
      const cycleIndex =
        Math.floor(Math.max(0, elapsed) / STAGE_DURATION_SECONDS) % flowDetails.length;
      const activeFlow = flowDetails[cycleIndex] || flowDetails[0];
      if (!hoveredStage) progressLabel.textContent = activeFlow.label;
      updateHover();
      updateStageEmphasis(activeFlow.stage);

      flows.forEach((flow) => {
        flow.particles.forEach(({ mesh, offset }, particleIndex) => {
          const progress = (elapsed * flow.speed + offset) % 1;
          mesh.position.copy(flow.curve.getPointAt(progress));
          const tangent = flow.curve.getTangentAt(progress).normalize();
          mesh.quaternion.setFromUnitVectors(particleUp, tangent);
          const cadence = 0.5 + Math.sin((progress + elapsed * 0.72) * Math.PI * 2) * 0.5;
          const pulse = 0.76 + cadence * 0.16 + (particleIndex % 3) * 0.025;
          mesh.scale.setScalar(pulse);
          mesh.material.emissiveIntensity = 0.12 + cadence * 0.26;
        });
      });

      let dominantStage = activeFlow.stage;
      let dominantAmount = -1;
      stageGroups.forEach((group, stage) => {
        const stageIndex = [...stageGroups.keys()].indexOf(stage);
        const activeTarget = group.userData.active ? 1 : 0;
        const hoverTarget = group.userData.hovered ? 1 : 0;
        group.userData.activeAmount = dampMotion(
          group.userData.activeAmount,
          activeTarget,
          2.2,
          frameDelta,
        );
        group.userData.hoverAmount = dampMotion(
          group.userData.hoverAmount,
          hoverTarget,
          4.6,
          frameDelta,
        );
        const activeAmount = group.userData.activeAmount;
        const hoverAmount = group.userData.hoverAmount;
        group.position.y =
          group.userData.baseY +
          Math.sin(elapsed * 0.68 + stageIndex) * 0.008 +
          activeAmount * (0.05 + Math.sin(elapsed * 1.35 + stageIndex) * 0.012) +
          hoverAmount * 0.075;
        group.scale.setScalar(1 + activeAmount * 0.024 + hoverAmount * 0.022);
        stageMeshes.get(stage).forEach((mesh) => {
          if (!mesh.material?.emissive) return;
          mesh.material.emissive.set(stageColors[stage]);
          mesh.material.emissiveIntensity = activeAmount * (0.095 + hoverAmount * 0.075);
        });
        stageMotionControllers[stage]?.(elapsed, activeAmount, hoverAmount);
        animateActivationHalo(stage, elapsed, activeAmount);
        const stageLabel = labelElements.get(stage);
        stageLabel?.style.setProperty("--loop-active-amount", activeAmount.toFixed(3));
        stageLabel?.classList.toggle("is-active", activeAmount >= 0.5);
        if (activeAmount > dominantAmount) {
          dominantAmount = activeAmount;
          dominantStage = stage;
        }
      });
      viewport.dataset.activeStage = dominantStage;

      camera.position.x = dampMotion(
        camera.position.x,
        cameraTarget.x,
        2.15,
        frameDelta,
      );
      camera.position.y = dampMotion(
        camera.position.y,
        7.55 + cameraTarget.y,
        2.15,
        frameDelta,
      );
      camera.lookAt(0, 0.72, 0.15);
      renderer.render(scene, camera);
      updateLabels();
    }

    function animate(frameTime) {
      if (destroyed) return;
      window.requestAnimationFrame(animate);
      const currentFrameTime = Number.isFinite(frameTime) ? frameTime : performance.now();
      const frameDelta = Math.max(
        0,
        Math.min((currentFrameTime - previousFrameTime) / 1000, 0.1),
      );
      previousFrameTime = currentFrameTime;
      if (!isVisible || manualPaused) return;
      elapsedTime += frameDelta;
      renderFrame(elapsedTime, frameDelta);
    }

    viewport.addEventListener("pointermove", (event) => {
      const bounds = renderer.domElement.getBoundingClientRect();
      pointer.x = ((event.clientX - bounds.left) / bounds.width) * 2 - 1;
      pointer.y = -((event.clientY - bounds.top) / bounds.height) * 2 + 1;
      cameraTarget.set(pointer.x * 0.12, pointer.y * 0.08);
    });
    viewport.addEventListener("pointerleave", () => {
      pointer.set(4, 4);
      cameraTarget.set(0, 0);
      hoveredStage = "";
      viewport.classList.remove("has-stage-hover");
      if (statusText) statusText.textContent = defaultStatusText;
      statusText?.classList.remove("is-inspecting");
    });

    motionToggle.addEventListener("click", () => {
      manualPaused = !manualPaused;
      const icon = motionToggle.querySelector("i");
      const label = motionToggle.querySelector("span");
      icon.className = `ph ${manualPaused ? "ph-play" : "ph-pause"}`;
      label.textContent = manualPaused ? "Play motion" : "Pause motion";
      motionToggle.setAttribute("aria-pressed", String(manualPaused));
      if (manualPaused) renderer.render(scene, camera);
    });

    const resizeObserver = new ResizeObserver(resize);
    resizeObserver.observe(viewport);
    const visibilityObserver = new IntersectionObserver(
      ([entry]) => {
        isVisible = entry.isIntersecting;
        if (isVisible && manualPaused) renderer.render(scene, camera);
      },
      { rootMargin: "180px 0px", threshold: 0.01 },
    );
    visibilityObserver.observe(root);

    window.addEventListener(
      "pagehide",
      () => {
        destroyed = true;
        resizeObserver.disconnect();
        visibilityObserver.disconnect();
        renderer.dispose();
      },
      { once: true },
    );

    resize();
    renderFrame(0);
    root.classList.remove("is-loading");
    root.classList.add("is-ready");
    window.requestAnimationFrame(animate);
  }
}
