// ======================================================================
// ======================================================================
// Smooth Scroll
// ======================================================================
// ======================================================================

const SmoothScroll = (target, speed, smooth, callback) => {
	if (target === document)
		target =
			document.scrollingElement ||
			document.documentElement ||
			document.body.parentNode ||
			document.body;

	const frame =
		target === document.body && document.documentElement
			? document.documentElement
			: target; // Safari is the new IE

	const state = {
		moving: false,
		pos: target.scrollTop || 0
	};

	const normalizeWheelDelta = e => {
		if (e.detail) {
			if (e.wheelDelta) {
				// Opera
				return e.wheelDelta / e.detail / 40 * (e.detail > 0 ? 1 : -1);
			} else {
				// Firefox
				return -e.detail / 3;
			}
		} else {
			// IE, Safari, Chrome
			if (e.wheelDelta) {
				return e.wheelDelta / 120;
			} else {
				// Also Firefox, for some reason...
				return -e.deltaY / 3;
			}
		}
	};

	const round = n => (n >= 0 ? Math.ceil(n) : Math.floor(n));

	const update = () => {
		const delta = round((state.pos - target.scrollTop) / smooth);

		state.moving = true;
		target.scrollTop += delta;

		callback(delta, target.scrollTop);

		if (Math.abs(delta) > 0.5) {
			requestAnimationFrame(update);
		} else {
			state.moving = false;
		}
	};

	const scrolled = e => {
		e.preventDefault();

		const delta = normalizeWheelDelta(e);

		state.pos += -delta * speed;
		state.pos = Math.floor(
			Math.max(0, Math.min(state.pos, target.scrollHeight - frame.clientHeight))
		);

		if (!state.moving) update();
	};

	const register = () =>
		target.addEventListener("wheel", scrolled, { passive: false });

	const unregister = () => {
		target.removeEventListener("wheel", scrolled);

		state.moving = false;
		state.pos = 0;
	};

	return { name: "SmoothScroll", register, unregister };
};

// ======================================================================
// ======================================================================
// Overlay Canvas
// ======================================================================
// ======================================================================

const OverlayCanvas = container => {
	const state = {
		scrollSpeed: 0,
		displace: 0
	};

	const getImages = () =>
		Array.from(document.body.getElementsByTagName("img")).map(source => ({
			source
		}));

	const lerp = (start, end, amt) => {
		return (1 - amt) * start + amt * end;
	};

	const register = () => {
		let { width: cw, height: ch, x: cx } = container.getBoundingClientRect();

		const app = new PIXI.Application({
			width: cw,
			height: ch,
			transparent: true,
			antialias: true,
			autoResize: true,
			resolution: window.devicePixelRatio
		});

		container.appendChild(app.view);

		const displacementSprite = new PIXI.Sprite.from(
			"https://i.imgur.com/rDhjAcJ.png"
		);

		displacementSprite.texture.baseTexture.wrapMode = PIXI.WRAP_MODES.REPEAT;
		displacementSprite.scale.x = 3;
		displacementSprite.scale.y = 3;

		const displacementFilter = new PIXI.filters.DisplacementFilter(
			displacementSprite
		);

		displacementFilter.padding = 200;
		displacementFilter.scale.x = 50;
		displacementFilter.scale.y = 50;

		app.stage.addChild(displacementSprite);
		app.stage.filters = [displacementFilter];

		const images = getImages();

		images.forEach(image => {
			const { source } = image;
			const { top, left, width, height } = source.getBoundingClientRect();
			const sprite = PIXI.Sprite.from(source.src);

			sprite.x = left - cx;
			sprite.y = top;
			sprite.width = width;
			sprite.height = height;

			app.stage.addChild(sprite);

			source.classList.add("replaced");

			image.sprite = sprite;
			image.x = left;
			image.y = top;
		});
		/*
		app.ticker.add(delta => {
			state.displace = lerp(state.displace, state.scrollSpeed, 0.1);

			displacementSprite.x += 1 * delta;

			displacementFilter.scale.x = state.displace * 2 + 8;
			displacementFilter.scale.y = state.displace * 2 + 8;
		});*/

		const smoothScroll = SmoothScroll(document, 53, 24, (delta, top) => {
			state.scrollSpeed = Math.abs(delta);

			images.forEach(({ sprite, y }) => {
				sprite.y = y - top;
			});
		});

		smoothScroll.register();

		window.addEventListener("resize", () => {
			const { width: nw, height: nh, x: nx } = container.getBoundingClientRect();

			app.renderer.resize(nw, nh);

			images.forEach(({ source, sprite }) => {
				const { top, left, width, height } = source.getBoundingClientRect();

				sprite.width = width;
				sprite.height = height;
				sprite.position.set(left - nx, top);
			});
		});
	};

	return { getImages, register };
};

// ======================================================================
// ======================================================================
// --- INIT ---
// ======================================================================
// ======================================================================

document.addEventListener("DOMContentLoaded", () => {
	const overlay = OverlayCanvas(document.querySelector("main"));
	const images = overlay.getImages();

	const checkAllImagesLoaded = () => {
		if (images.every(({ source }) => source.complete)) {
			overlay.register();
		}
	};

	images.forEach(({ source }) =>
		source.addEventListener("load", checkAllImagesLoaded)
	);

	checkAllImagesLoaded();
});
