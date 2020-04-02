/**
 * Summary.
 *
 * Associate table of content with corresponding header.
 *
 * @link   https://github.com/Ynjxsjmh/toc-backref
 * @author Ynjxsjmh
 * @since  2020.03.27
 */


(($) => {
  String.prototype.format = function() {
    var formatted = this;
    for (var i = 0; i < arguments.length; i++) {
      var regexp = new RegExp('\\{'+i+'\\}', 'gi');
      formatted = formatted.replace(regexp, arguments[i]);
    }
    return formatted;
  };

  let tocBackRefProxy = (contentSelector, hTagsArr, tocUlSelector='undefined', modest=true) => {
    if (tocUlSelector == 'undefined') {
      var isTocExist = false;
      var possibleUlSelector = contentSelector + " ul:first";
      var ul = $(possibleUlSelector);

      if ($(ul).length) {
        var li = $("li", ul).first();

        if ($(li).length) {
          var a = $(li).find('a:first');
          var content = $(contentSelector);
          var h1 = content.find("h1").first();

          if ($(h1).text() == $(a).text()) {
            isTocExist = true;
          }
        }
      }

      if (isTocExist) {
        generateBackRef(possibleUlSelector, contentSelector, hTagsArr, modest);
      } else {
        generateToc(contentSelector, hTagsArr, modest);
      }
    } else {
      generateBackRef(tocUlSelector, contentSelector, hTagsArr, modest);
    }
  };

  let generateBackRef = (tocUlSelector, contentSelector, hTagsArr, modest=true) => {
    /**
     * 1. toc part
     *    1.1 get the href of li
     *    1.2 get the text of li
     *    1.3 get the id of li. If it doesn't have one, generate for it
     * 2. header part
     *    2.1 get the id of header
     *    2.2 get the text of header
     *    2.3 set the href of header to 1.3
     *        When to set?
     *        - if 1.1 == 2.1
     *        - if 1.1 != 2.1, judge if 1.2 == 2.2
     */

    var tocUl = $(tocUlSelector), tocId, tocBackRef;
    var tocIdPrefix = "toc";
    var liList = $("li", tocUl), li;
    var content = $(contentSelector);
    var hList = content.find(hTagsArr.join(',')), hId, hText, hTagName;

    hList.each(function (index) {
      tocId = tocIdPrefix + index;
      hId = $(this).prop('id');
      hText = $(this).text();

      for (var i = 0; i < liList.length; ++i) {
        li = liList.eq(i);
        var a = $(li).find('a:first');
        aId = $(a).prop('id');
        aHref = $(a).prop('href');
        aText = $(a).text();

        if (aHref == hId || aText == hText) {
          if (aId == '' || aId == null || aId == 'undefined') {
            aId = tocId;
            $(a).attr("id", aId);
          }

          if (modest) {
            tocBackRef = $("<a class='toc-backref p-1' href='#{0}' rel='nofollow' target='_self'></a>".format(aId));
          } else {
            tocBackRef = $("<a class='toc-backref p-1' href='#{0}' rel='nofollow' target='_self'>{1}</a>".format(aId, hText));
            $(this).text("");
          }

          $(this).append(tocBackRef);

          liList.splice(i, 1);
          break;
        }
      }
    });
  };

  let generateToc = ( contentSelector, hTagsArr, modest=true) => {
    var tocUl = $('<ul class="toc-body"></ul>'), tocId, tocLi, tocRef, tocBackRef;
    var tocIdPrefix = "toc";
    var content = $(contentSelector), hId, hText, hTagName;
    var hList = content.find(hTagsArr.join(','));

    hList.each(function (index) {
      tocId = tocIdPrefix + index;
      hText = $(this).text();

      if (modest) {
        tocBackRef = $("<a class='toc-backref p-1' href='#{0}' rel='nofollow' target='_self'></a>".format(tocId));
      } else {
        tocBackRef = $("<a class='toc-backref p-1' href='#{0}' rel='nofollow' target='_self'>{1}</a>".format(tocId, hText));
        $(this).text("");
      }

      $(this).append(tocBackRef);

      hId = $(this).prop('id');
      if (hId == undefined || hId == '' || hId == null) {
        var headingIdPrefix = "header";
        $(this).attr("id", headingIdPrefix + index);
        hId = $(this).prop('id');
      } else {
        // pass
      }

      tocRef = $('<a class="reference internal" id="{0}" href="#{1}">{2}</a>'.format(tocId, hId, hText));
      hTagName = $(this).prop('tagName').toLowerCase();
      tocLi = $('<li class="{0}_nav"></li>'.format(hTagName)).append(tocRef);
      tocUl.append(tocLi);
    });

    $(contentSelector).prepend(tocUl);

    return true;
  };

  $.extend({ tocBackRefProxy });

})($);
