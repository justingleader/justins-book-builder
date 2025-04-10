## Forest Image

![](ingtotheforest.jpg)

::: {.attribution}
Photo courtesy of [@ingtotheforest](https://unsplash.com/@ingtotheforest)
:::
```

Note that the `revealjs-plugins` key references the `attribution` extension, which will implemented in the `_extensions/attribution` directory.

The `_extension.yml` file indicates that the extension is making available a Revealjs plugin along with the plugin name, script, and style-sheets (note that the plugin name is not arbitrary, it will be whatever name is used within the script that implements the plugin, in this case `RevealAttribution`):

**_extensions/attribution/_extension.yml**
```yaml
title: Attribution
author: Roland Schmehl
version: 0.1.0
quarto-required: ">=1.2.0"

contributes:
  revealjs-plugins:
    - name: RevealAttribution
      script:
        - attribution.js
      stylesheet:
        - attribution.css
```

The `attribution.js` file contains the implementation of the Plugin using the Revealjs Plugin API:

**_extensions/attribution/attribution.js**
```javascript
window.RevealAttribution = window.RevealAttribution || {
  id: 'RevealAttribution',
  init: function(deck) {
    initAttribution(deck);
  }
};

const initAttribution = function(Reveal){

  var ready = false;
  var resize = false;
  var scale = 1;

  window.addEventListener( 'ready', function( event ) {
    var content;
    // Remove configured margin of the presentation
    var attribution = document.getElementsByClassName("attribution");
    var width = window.innerWidth;
    var configuredWidth = Reveal.getConfig().width;
    var configuredHeight = Reveal.getConfig().height;

    scale = 1/(1 - Reveal.getConfig().margin);

    for (var i = 0; i < attribution.length; i++) {
      content = attribution[i].innerHTML;
      attribution[i].style.width = configuredWidth + "px";
      attribution[i].style.height = configuredHeight + "px";
      attribution[i].innerHTML = "<span class='content'>" + content + "</span>";
      attribution[i].style.transform = 'translate( -50%, -50% ) scale( ' + scale*100 + '% ) rotate(-180deg)';
    }
    // Scale with cover class to mimic backgroundSize cover
    resizeCover()
  });

  window.addEventListener( 'resize', resizeCover );

  function resizeCover() {
    // Scale to mimic backgroundSize cover
    var attribution = document.getElementsByClassName("attribution");
    var xScale = window.innerWidth / Reveal.getConfig().width;
    var yScale = window.innerHeight / Reveal.getConfig().height;
    var s = 1;
    if (xScale > yScale) {
      // The div fits perfectly in x axis, stretched in y
      s = xScale / yScale;
    }
    for (var i = 0; i < attribution.length; i++) {
      attribution[i].style.transform = 'translate( -50%, -50% ) scale( ' + s*scale*100 + '% ) rotate(-180deg)';
    }
  }
};
```

Finally, `attribution.css` includes the CSS that repositions and rotates the element with class `.attribution` on the far right side of the slide:

**_extensions/attribution/attribution.css**
```css
/* Attribution plugin: text along the right edge of the viewport */
.attribution {
  position: absolute;
  top: 50%;
  bottom: auto;
  left: 50%;
  right: auto;
  font-size: 0.4em;
  pointer-events: none;
  text-align: center;
  writing-mode: vertical-lr;
  transform: translate(-50%, -50%) scale(100%) rotate(-180deg);
}

/* Attribution plugin: activate pointer events for attribution text only */
.attribution .content {
  pointer-events: auto;
}
```

