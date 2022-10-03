'use strict';

var defaultOptions = {
	// String: Selector to indicate each ticker item. Must be a direct child of the ticker element
	item: 'div',

	// Boolean: Toggles whether the ticker should pause if the mouse cursor is over it
	pauseOnHover: false,

	// Number: Speed of ticker in Pixels/Second.
	speed: 60,

	// String: (track|item) Sets whether ticker breaks when it hits a new item or if the track has reset
	pauseAt: '',

	// Number: Pause duration for pauseAt
	delay: 500
};

var rafSupported = true;

// Check for Transform Support | Credit: https://stackoverflow.com/questions/7212102/detect-with-javascript-or-jquery-if-css-transform-2d-is-available
function getSupportedTransform() {
	var prefixes = 'transform WebkitTransform MozTransform OTransform msTransform'.split(' ');
	var div = document.createElement('div');
	for (var i = 0; i < prefixes.length; i++) {
		if (div && div.style[prefixes[i]] !== undefined) {
			return prefixes[i];
		}
	}
	return false;
}

// Polyfill for requestAnimationFrame | Credit: https://stackoverflow.com/questions/5605588/how-to-use-requestanimationframe
var requestAnimFrame = function () {
	return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function ( /* function */callback) {
		rafSupported = false;
		window.setTimeout(callback, 1000 / 60);
	};
}();

// Doing it this way to remove logging code from production entirely.

var logger = function logger(location) {
	{
		return function () {};
	}
};

/* This is where the magic happens */
var log$1 = logger('brain');

var FPSs = [60];

var tickers = [];

function getFps() {
	//return 60;
	if (!rafSupported) return 60;
	var l = FPSs.length;
	return FPSs.reduce(function (a, b) {
		return a + b;
	}) / l;
}

var brain = {
	get fps() {
		return getFps();
	},
	get tickers() {
		return tickers;
	},
	init: function init($) {
		var frameCount = 0;
		var fpsInterval = 0;

		requestAnimFrame(function tick() {
			frameCount++;
			if (tickers.length) tickers.forEach(function (t) {
				return t.advance();
			});

			requestAnimFrame(tick);
		});

		// Monitor fps
		if (rafSupported) {
			var fpsMon = void 0;
			$(window).on('load focus', function () {
				log$1('Frame Count: %d, FPS Interval: %d', frameCount, fpsInterval);
				if (!fpsMon && document.hasFocus()) {
					fpsInterval = frameCount;
					fpsMon = setInterval(function () {
						var fps = frameCount - fpsInterval;
						FPSs.push(fps);

						while (FPSs.length > 10) {
							FPSs.shift();
						}log$1(getFps());

						fpsInterval = frameCount;
					}, 1000);
				}
			}).on('blur', function () {
				clearInterval(fpsMon);
				fpsMon = null;
			});
		}
	}
};

var asyncGenerator = function () {
  function AwaitValue(value) {
    this.value = value;
  }

  function AsyncGenerator(gen) {
    var front, back;

    function send(key, arg) {
      return new Promise(function (resolve, reject) {
        var request = {
          key: key,
          arg: arg,
          resolve: resolve,
          reject: reject,
          next: null
        };

        if (back) {
          back = back.next = request;
        } else {
          front = back = request;
          resume(key, arg);
        }
      });
    }

    function resume(key, arg) {
      try {
        var result = gen[key](arg);
        var value = result.value;

        if (value instanceof AwaitValue) {
          Promise.resolve(value.value).then(function (arg) {
            resume("next", arg);
          }, function (arg) {
            resume("throw", arg);
          });
        } else {
          settle(result.done ? "return" : "normal", result.value);
        }
      } catch (err) {
        settle("throw", err);
      }
    }

    function settle(type, value) {
      switch (type) {
        case "return":
          front.resolve({
            value: value,
            done: true
          });
          break;

        case "throw":
          front.reject(value);
          break;

        default:
          front.resolve({
            value: value,
            done: false
          });
          break;
      }

      front = front.next;

      if (front) {
        resume(front.key, front.arg);
      } else {
        back = null;
      }
    }

    this._invoke = send;

    if (typeof gen.return !== "function") {
      this.return = undefined;
    }
  }

  if (typeof Symbol === "function" && Symbol.asyncIterator) {
    AsyncGenerator.prototype[Symbol.asyncIterator] = function () {
      return this;
    };
  }

  AsyncGenerator.prototype.next = function (arg) {
    return this._invoke("next", arg);
  };

  AsyncGenerator.prototype.throw = function (arg) {
    return this._invoke("throw", arg);
  };

  AsyncGenerator.prototype.return = function (arg) {
    return this._invoke("return", arg);
  };

  return {
    wrap: function (fn) {
      return function () {
        return new AsyncGenerator(fn.apply(this, arguments));
      };
    },
    await: function (value) {
      return new AwaitValue(value);
    }
  };
}();





var classCallCheck = function (instance, Constructor) {
  if (!(instance instanceof Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
};

var createClass = function () {
  function defineProperties(target, props) {
    for (var i = 0; i < props.length; i++) {
      var descriptor = props[i];
      descriptor.enumerable = descriptor.enumerable || false;
      descriptor.configurable = true;
      if ("value" in descriptor) descriptor.writable = true;
      Object.defineProperty(target, descriptor.key, descriptor);
    }
  }

  return function (Constructor, protoProps, staticProps) {
    if (protoProps) defineProperties(Constructor.prototype, protoProps);
    if (staticProps) defineProperties(Constructor, staticProps);
    return Constructor;
  };
}();

/* Ticker Class - Controls each instance of a ticker. */

var log$2 = logger('class');

/* TODO: Port over to private fields
 * - Requires Gulp setup
 **/

var Ticker = function () {
	function Ticker(elem, settings) {
		classCallCheck(this, Ticker);

		this.elem = elem;

		this.settings = settings;

		this.__offset = 0;
		this.__pauseTracker = 0;

		this.build();
	}

	createClass(Ticker, [{
		key: 'build',
		value: function build() {
			var _this = this;

			if (!this.started) {
				this.started = true;

				//region Build Track
				var track = document.createElement('div'); // <div class="js-ticker-track">;
				track.className = 'js-ticker-track';

				this.elem.addClass('js-ticker');
				this.elem.children(this.settings.item).addClass('js-ticker-item').appendTo(track);

				this.elem.append(track);
				//endregion

				//region Init Variables
				this.track = this.elem.find('.js-ticker-track');
				this.__items = this.track.children('.js-ticker-item');

				this.__first = this.__items.first();
				this.__first.attr('data-first', true);
				//endregion

				//region Clone For Scale
				var targetWidth = this.elem.width() + this.__first.width();

				log$2('(Pre Clones) Target Width: %d, Actual: %d', targetWidth, this.elem[0].scrollWidth);

				while (this.elem[0].scrollWidth < targetWidth) {
					this.__items.each(function (i) {
						_this.track.append(_this.__items.eq(i).clone());
					});
				}

				log$2('(Post Clones) Target Width: %d, Actual: %d', targetWidth, this.elem[0].scrollWidth);
				//endregion

				//region Init Events
				// Insurance to prevent doubling up on enter triggers
				/* FIXME: This looks... un... safe. */
				var initHover = function initHover() {
					_this.elem.one('mouseenter', function () {
						_this.__pauseTracker++;
						_this.elem.one('mouseleave', function () {
							_this.__pauseTracker--;
							initHover();
						});
					});
				};

				if (this.settings.pauseOnHover) initHover();

				/* TODO: Pause on focus and reset slider position for ADA
     * - Also need a solution on keyboard navigation
     **/
				//endregion

				//region Enable Ticker
				this.elem.addClass('active');
				this.elem.data('ticker', this);

				brain.tickers.push(this);
				//endregion
			}
		}
	}, {
		key: 'advance',
		value: function advance() {
			var _this2 = this;

			this.__width = this.__first.outerWidth();
			if (!this.__pauseTracker) {

				this.__offset += this.settings.speed / brain.fps;

				/* TODO: Need a solution to go in reverse */
				if (this.__offset > this.__width) {
					this.__offset = 0;
					this.__first.appendTo(this.track);
					this.__first = this.track.children('.js-ticker-item').first();
					if (this.settings.pauseAt === 'item' || this.settings.pauseAt === 'track' && this.__first.data('first')) {
						this.__pauseTracker++;
						setTimeout(function () {
							return _this2.__pauseTracker--;
						}, this.settings.delay);
					}
				}

				var transformProp = getSupportedTransform();

				if (transformProp) {
					this.track.css(transformProp, 'translateX(' + -this.__offset + 'px)');
				} else {
					this.track.css('left', -this.__offset + 'px');
				}
			}
		}
	}, {
		key: 'pause',
		value: function pause() {
			if (!this.__manuallyPaused) {
				this.__pauseTracker++;
				this.__manuallyPaused = true;
			}
		}
	}, {
		key: 'play',
		value: function play() {
			if (this.__manuallyPaused) {
				this.__pauseTracker--;
				this.__manuallyPaused = false;
			}
		}
	}, {
		key: 'toggle',
		value: function toggle() {
			if (this.__manuallyPaused) {
				this.play();
			} else {
				this.pause();
			}
		}
	}], [{
		key: 'version',
		get: function get$$1() {
			return '0.0.1';
		}
	}]);
	return Ticker;
}();

/**
 * Small jQuery Plugin create by Quangdao Nguyen
 */

var log = logger('entry');

(function ($) {
	'use strict';

	if (!$) return console.warn('Whoa there, buddy! Looks like you included the jQuery Ticker plugin without including jQuery first.');

	$.ticker = function (elem, settings) {
		return new Ticker($(elem), settings);
	};

	$.fn.ticker = function () {
		var overrides = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};

		return this.each(function () {
			$.ticker(this, $.extend(true, {}, defaultOptions, overrides));
		});
	};

	brain.init($);
})(typeof jQuery !== 'undefined' ? jQuery : null);
