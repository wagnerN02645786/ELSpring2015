/*
 * Bootstrap Image Gallery JS Demo 3.0.1
 * https://github.com/blueimp/Bootstrap-Image-Gallery
 *
 * Copyright 2013, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
 */

/*jslint unparam: true */
/*global blueimp, $ */

$(function () {
    'use strict';
    // Load demo images from flickr:
    $.ajax({
        //url: 'https://api.flickr.com/services/rest/',
        url: './gallery.php',
        type: "POST",
        dataType: 'json',
        jsonp: 'jsoncallback'
        // success: function(data)
        // {
        //     $('#links').html(JSON.stringify(data));
        //     console.log(json);
        // }
    }).done(
        function (result) {
            var linksContainer = $('#links'), baseUrl;
        // Add the demo images as links with thumbnails to the page:
        $.each(result, function (index, photo) {
            // baseUrl = 'http://farm' + photo.farm + '.static.flickr.com/' +
            //     photo.server + '/' + photo.id + '_' + photo.secret;
            baseUrl = photo.baseurl;
             $('<a/>')
                 .append($('<img>').prop('src', baseUrl).attr('height', '75').attr('width', '75'))
                 .prop('href', baseUrl)
                 .prop('title', photo.title)
                 .attr('data-gallery', '')
                 .appendTo(linksContainer);
        });
    }).fail ( function() {alert("Error")
    });

    $('#borderless-checkbox').on('change', function () {
        var borderless = $(this).is(':checked');
        $('#blueimp-gallery').data('useBootstrapModal', !borderless);
        $('#blueimp-gallery').toggleClass('blueimp-gallery-controls', borderless);
    });

    $('#fullscreen-checkbox').on('change', function () {
        $('#blueimp-gallery').data('fullScreen', $(this).is(':checked'));
    });

    $('#image-gallery-button').on('click', function (event) {
        event.preventDefault();
        blueimp.Gallery($('#links a'), $('#blueimp-gallery').data());
    });

});
