function getBackgroundSize(elem) {
    var computedStyle = getComputedStyle(elem),
        image = new Image(),
        src = computedStyle.backgroundImage.replace(/url\((['"])?(.*?)\1\)/gi, '$2'),
        cssSize = computedStyle.backgroundSize,
        elemW = parseInt(computedStyle.width.replace('px', ''), 10),
        elemH = parseInt(computedStyle.height.replace('px', ''), 10),
        elemDim = [elemW, elemH],
        computedDim = [],
        ratio;
    image.src = src;
    ratio = image.width > image.height ? image.width / image.height : image.height / image.width;
    cssSize = cssSize.split(' ');
    computedDim[0] = cssSize[0];
    computedDim[1] = cssSize.length > 1 ? cssSize[1] : 'auto';
    if (cssSize[0] === 'cover') {
        if (elemDim[0] > elemDim[1]) {
            if (elemDim[0] / elemDim[1] >= ratio) {
                computedDim[0] = elemDim[0];
                computedDim[1] = 'auto';
            } else {
                computedDim[0] = 'auto';
                computedDim[1] = elemDim[1];
            }
        } else {
            computedDim[0] = 'auto';
            computedDim[1] = elemDim[1];
        }
    } else if (cssSize[0] === 'contain') {
        // Width is less than height
        if (elemDim[0] < elemDim[1]) {
            computedDim[0] = elemDim[0];
            computedDim[1] = 'auto';
        } else {
            if (elemDim[0] / elemDim[1] >= ratio) {
                computedDim[0] = 'auto';
                computedDim[1] = elemDim[1];
            } else {
                computedDim[1] = 'auto';
                computedDim[0] = elemDim[0];
            }
        }
    } else {
        for (var i = cssSize.length; i--;) {
            if (cssSize[i].indexOf('px') > -1) {
                computedDim[i] = cssSize[i].replace('px', '');
            } else if (cssSize[i].indexOf('%') > -1) {
                computedDim[i] = elemDim[i] * (cssSize[i].replace('%', '') / 100);
            }
        }
    }
    if (computedDim[0] === 'auto' && computedDim[1] === 'auto') {
        computedDim[0] = image.width;
        computedDim[1] = image.height;
    } else {
        ratio = computedDim[0] === 'auto' ? image.height / computedDim[1] : image.width / computedDim[0];
        computedDim[0] = computedDim[0] === 'auto' ? image.width / ratio : computedDim[0];
        computedDim[1] = computedDim[1] === 'auto' ? image.height / ratio : computedDim[1];
    }
    return {
        width: computedDim[0],
        height: computedDim[1]
    };
}


$(document).ready(function () {

    var height = getBackgroundSize($('.site_bg_img').get(0))['height'];
    var container_height = $(".site_bg").height();


    $(window).scroll(function () {
        setBackgroundPosition();
    });
    $(window).resize(function () {
        setBackgroundPosition();
    });

    console.log();
    function setBackgroundPosition() {

        if ((container_height + parseInt($(window).scrollTop())) <= getBackgroundSize($('.site_bg_img').get(0))['height']) {
            $(".site_bg_img").css("background-position", 50 + "% +" + (container_height + parseInt($(window).scrollTop())) + "px ");
        }
    }
});
