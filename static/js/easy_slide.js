/*
https://github.com/IvanShabanov/EasySlides

EasySlides - слайдер
Autor 2017-2024 Shabanov Ivan (Шабанов Иван)
Usage:

   $('.slider').EasySlides({
        'autoplay': true,
        'timeout': 3000,
        'show': 5, //Сколь-ко позывать слайдов (по умолчанию 5: 1-активный, 2-предыдущих и 2-следующих)
        'vertical': false,  //Если True то слайдер вертикальный, слайды листаются движением вверх/вниз
        'reverse': false, //Перевернутый слайдер
        'touchevents': true, //Вкючено ли события на прикосновения к сладеру (листания и т.п)
        'delayaftershow': 300, //Задержка после смены слайдера, в это время слайдер нельзя листать
        'stepbystep': true, //При клике на далекий слайд перейти к нему последовательно, а не сразу
        'startslide': 0,  //Стартовый слайд
        'beforeshow': function () {},
        'aftershow': function () {},
        'onclick': function (slide) {},
        'disabledefaultclick': false,
    });

*/
(function ($) {

    $.fn.EasySlides = function (options) {
        var settings = $.extend({
            'autoplay': false,
            'timeout': 3000,
            'show': 5,
            'vertical': false,
            'reverse': false,
            'touchevents': true,
            'delayaftershow': 300,
            'stepbystep': true,
            'loop': true,
            'startslide': 0,
            'distancetochange': 10,
            'beforeshow': function () {},
            'aftershow': function () {},
            'onclick': function () { },
            'disabledefaultclick': false,
        }, options);
        return this.each(function () {
            var this_slider = this;
            var EasySlidesTimer;
            var EasySlidesCanChange = true;

            var count = $(this_slider).children('*:not(.next_button, .prev_button, .nav_indicators)').length;
            var cur_slide = 0;
            var mousedowned = false;
            var need_slide = 0;
            var slides;
            if (count > 0) {

                while (count < settings['show']) {
                    var html = $(this_slider).html();
                    $(html).appendTo(this_slider);
                    $(this_slider).children('.next_button:eq(0), .prev_button:eq(0), .nav_indicators:eq(0)').remove();
                    slides = $(this_slider).children('*:not(.next_button, .prev_button, .nav_indicators)');

                    count = $(slides).length;
                }
                slides = $(this_slider).children('*:not(.next_button, .prev_button, .nav_indicators)');

                if ($(this_slider).children('.nav_indicators').length > 0) {
                    var nav_indicators = '<ul>';
                    while (need_slide < count) {
                        need_slide++;
                        nav_indicators = nav_indicators + '<li>' + need_slide + '</li>';
                    }
                    nav_indicators = nav_indicators + '</ul>';
                    $(this_slider).children('.nav_indicators').html(nav_indicators);
                    need_slide = 0
                }
                var EasySlidesLoopToNeeded = function () {
                    var next;
                    var left = need_slide - cur_slide;
                    var right = cur_slide - need_slide
                    if (settings['loop'] == true) {
                        if (left < 0) {
                            left = left + count;
                        }
                        if (right < 0) {
                            right = right + count;
                        }
                    }
                    if (cur_slide != need_slide) {
                        if (settings['loop'] == true) {
                            if ((left) < (right)) {
                                next = cur_slide + 1;
                            } else {
                                next = cur_slide - 1;
                            }
                        } else {
                            if (left > 0) {
                                next = cur_slide + 1;
                            } else {
                                next = cur_slide - 1;
                            }
                        }
                        EasySlidesNext(next);
                        setTimeout(EasySlidesLoopToNeeded, settings['delayaftershow']);
                    }
                }
                var EasySlidesNext = function (nextslide) {
                    if (EasySlidesCanChange) {
                        EasySlidesCanChange = false;
                        setTimeout(function () {
                            EasySlidesCanChange = true;
                        }, settings['delayaftershow']);
                        clearTimeout(EasySlidesTimer);
                        if (typeof settings['beforeshow'] == 'function') {
                            settings['beforeshow']();
                        }
                        var i = 0;
                        if (count > 0) {
                            if (typeof nextslide == 'number') {
                                cur_slide = nextslide;
                            } else {
                                cur_slide++;
                                nextslide = cur_slide;
                            }
                            if (settings['loop'] == true) {
                                while (cur_slide < 0) {
                                    cur_slide = cur_slide + count;
                                }
                                while (cur_slide >= count) {
                                    cur_slide = cur_slide - count;
                                }
                                while (nextslide < 0) {
                                    nextslide = nextslide + count;
                                }
                                while (nextslide >= count) {
                                    nextslide = nextslide - count;
                                }

                            } else {
                                if (cur_slide < 0) {
                                    cur_slide = 0;
                                }
                                if (cur_slide >= count) {
                                    cur_slide = count - 1;
                                }
                                if (nextslide < 0) {
                                    nextslide = 0;
                                }
                                if (nextslide >= count) {
                                    nextslide = count - 1;
                                }
                            }
                            $(this_slider).children('.nav_indicators').find('ul').find('li').removeClass('active');

                            $(this_slider).find('.nav_indicators ul li:nth-child(' + (nextslide + 1) + ')').addClass('active');
                            i = 0;
                            /*
                            $(this_slider).children('*:not(.next_button, .prev_button, .nav_indicators)').each(function() {
                            */
                            $(slides).each(function () {


                                var cssclass = '';
                                var icount = 0;
                                icount = i - nextslide;
                                while (icount < 0) {
                                    icount = icount + count;
                                }

                                while (icount > count) {
                                    icount = icount - count;
                                }
                                if (icount == 0) {
                                    cssclass = 'active';
                                    $(this_slider).find('.' + cssclass + ':not(.nav_indicators ul li)').removeClass(cssclass);
                                    $(this).removeClass('hidden');
                                    $(this).addClass(cssclass);
                                } else if (icount < settings['show'] / 2) {
                                    cssclass = 'next' + icount;
                                    $(this_slider).find('.' + cssclass).removeClass(cssclass);
                                    $(this).removeClass('hidden');
                                    $(this).addClass(cssclass);
                                } else if (icount > count - (settings['show'] / 2)) {
                                    cssclass = 'prev' + (count - icount);
                                    $(this_slider).find('.' + cssclass).removeClass(cssclass);
                                    $(this).removeClass('hidden');
                                    $(this).addClass(cssclass);
                                } else {
                                    $(this).addClass('hidden');
                                }

                                if ((Math.abs(i - nextslide) > (settings['show'] / 2)) && (settings['loop'] == false)) {
                                    var icnt = 1;
                                    while (icnt < settings['show'] / 2) {
                                        cssclass = 'next' + icnt;
                                        if ($(this).hasClass(cssclass) ) {
                                            $(this).removeClass(cssclass)
                                        };
                                        cssclass = 'prev' + icnt;
                                        if ($(this).hasClass(cssclass) ) {
                                            $(this).removeClass(cssclass)
                                        };
                                        icnt ++;
                                    };
                                    $(this).addClass('hidden');
                                }
                                i++;
                            });
                            if (settings['autoplay']) {
                                clearTimeout(EasySlidesTimer);
                                EasySlidesTimer = setTimeout(function () {
                                    EasySlidesNext();
                                }, settings['timeout']);
                            }
                        }
                        if (typeof settings['aftershow'] == 'function') {
                            settings['aftershow']();
                        }

                    }
                }
                EasySlidesNext(settings['startslide']);
                /*
                $(this_slider).children(':not(.next_button, .prev_button, .nav_indicators)').click(function () {
                */
                $(slides).click(function () {
                    if (typeof settings['onclick'] == 'function') {
                        settings['onclick'](this);
                    }
                    if (settings['disabledefaultclick']) {
                        return;
                    }
                    need_slide = $(this_slider).children().index(this);
                    if (settings['stepbystep']) {
                        EasySlidesLoopToNeeded()
                    } else {
                        EasySlidesNext(need_slide);
                    }
                });
                $(this_slider).children('.nav_indicators').find('ul').find('li').click(function () {
                    need_slide = $(this_slider).find('.nav_indicators ul li').index(this);
                    if (settings['stepbystep']) {
                        EasySlidesLoopToNeeded()
                    } else {
                        EasySlidesNext(need_slide);
                    }
                });

                $(this_slider).find('.next_button').click(function () {
                    EasySlidesCanChange = true;
                    EasySlidesNext();
                });
                $(this_slider).find('.prev_button').click(function () {
                    EasySlidesCanChange = true;
                    cur_slide--;
                    EasySlidesNext(cur_slide);
                });
                if (settings['touchevents']) {
                    var EasySliderMoved = function (xcur, ycur) {
                        var offset = $(slides).find('.active').offset();
                        var left = 0;
                        var top = 0;
                        if (typeof offset !== 'undefined') {
                            left = offset.left;
                            top = offset.top;
                        }

                        var p0 = $(this_slider).data('posstart'),
                            p1 = {
                                x: xcur,
                                y: ycur,
                                l: left,
                                t: top,
                            },
                            d = 0;
                        if (typeof p0 === 'undefined') {
                            p0 = p1;
                            $(this_slider).data('posstart', p1);
                        }

                        if (settings['vertical']) {
                            d = p1.y - p0.y;
                            top = p0.t + d;
                            //$(this_slider).find('.active:not(.nav_indicators ul li)').offset({'top': top});
                        } else {
                            d = p1.x - p0.x;
                            left = p0.l + d;
                            //$(this_slider).find('.active:not(.nav_indicators ul li)').offset({'left': left});
                        }
                        if (settings['reverse']) {
                            d = -d;
                        }
                        if ((Math.abs(d) > settings['distancetochange']) && (EasySlidesCanChange)) {
                            $(this_slider).data('posstart', p1);

                            if (d > 0) {
                                cur_slide--;
                            } else {
                                cur_slide++;
                            }
                            EasySlidesNext(cur_slide);
                        }
                    }
                    /*События*/
                    $(this_slider).bind('mousemove', function (e) {
                        e.preventDefault();
                        if (e.buttons > 0) {
                            EasySliderMoved(e.pageX, e.pageY);
                            mousedowned = true;
                        } else {
                            if (mousedowned) {
                                EasySliderMoved(e.pageX, e.pageY);
                                $(this_slider).removeData('posstart');
                                mousedowned = false;
                            }
                        }
                    });
                    $(this_slider).bind('mouseup', function (e) {
                        e.preventDefault();
                        if (mousedowned) {
                            EasySliderMoved(e.pageX, e.pageY);
                            $(this_slider).removeData('posstart');
                            mousedowned = false;
                        }
                    })

                    $(this_slider).bind('touchmove', function (e) {
                        var touch = e.originalEvent.touches[0] || e.originalEvent.changedTouches[0];
                        EasySliderMoved(touch.pageX, touch.pageY);
                    });
                    $(this_slider).bind('touchend', function (e) {
                        $(this_slider).removeData('posstart');
                    });

                }
            }
        });
    }
})(jQuery);
