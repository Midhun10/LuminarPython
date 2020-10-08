jQuery(document).ready(function($){
	"use strict";

	$.fn.hasAttr = function(name) {  
	   return this.attr(name) !== undefined;
	};	
	
	/* PRELOADER */
	$(window).load(function(){
		$('.preloader').addClass('animation');
		setTimeout(function(){
			$('.preloader').remove();
		}, 500);
	});

	/* PARSE STYLES */
	$('.travelico_style').each(function(){
		alert( $(this).html() );
	});

	/* PROGRESS BARS */
	$('.progress').each(function(){
		var $this = $(this);
		$this.waypoint(function() {
			$this.find('.progress-bar').progressbar(); 
		}, { offset: '100%' });
	});

	/* COUNTERS */
	$('.counter').each(function(){
		$(this).counterUp({
	    	delay: 10,
	    	time: 1000
	    });
	});	

	/* TESTIMONIALS */
	$('.testimonials').owlCarousel({ 
		autoPlay: true, 
		navigation: true,
		navigationText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
		pagination: false,
		items: 1,
		singleItem: true
	});

	/* CLIENTS */
	$('.clients').each(function(){
		var $this = $(this);
		var autoplay = $this.data( 'autoplay' );
		if( autoplay == '' ){
			autoplay = false;
		}
		$this.owlCarousel({ 
			autoPlay: autoplay,
			items: $this.data( 'items' ),
			pagination: false
		});
	});

	/* PARALALX SECTIONS */
	$(window).stellar({
	    horizontalScrolling: false
	});

	/* KNOBS */
 	$('.knob').each(function () {
 		var $this = $(this);
		$this.knob({ 
			readOnly: true,
			draw: function(){
                if(this.$.data('skin') == 'tron') {
                    var a = this.angle(this.cv)  // Angle
                        , sa = this.startAngle          // Previous start angle
                        , sat = this.startAngle         // Start angle
                        , ea                            // Previous end angle
                        , eat = sat + a                 // End angle
                        , r = true;

                    this.g.lineWidth = this.lineWidth;

                    this.o.cursor
                        && (sat = eat - 0.3)
                        && (eat = eat + 0.3);

                    if (this.o.displayPrevious) {
                        ea = this.startAngle + this.angle(this.value);
                        this.o.cursor
                            && (sa = ea - 0.3)
                            && (ea = ea + 0.3);
                        this.g.beginPath();
                        this.g.strokeStyle = this.previousColor;
                        this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sa, ea, false);
                        this.g.stroke();
                    }

                    this.g.beginPath();
                    this.g.strokeStyle = r ? this.o.fgColor : this.fgColor ;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sat, eat, false);
                    this.g.stroke();

                    this.g.lineWidth = 2;
                    this.g.beginPath();
                    this.g.strokeStyle = this.o.fgColor;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth + 1 + this.lineWidth * 2 / 3, 0, 2 * Math.PI, false);
                    this.g.stroke();

                    return false;
                }				
			}
		});
 		$this.waypoint(function(){ 			
 			if( !$this.hasClass('animated') ){
		       	var myVal = $this.data("target");
		       	$this.addClass('animated');
		        $({
		 		    value: 0
		       	}).animate(
		       		{
						value: myVal
					}, 
					{
						duration: 2000,
		           		easing: 'swing',
		           		step: function () {
		               		$this.val(Math.ceil(this.value)).trigger('change');
		           		}
		       		}
		       	);
		       }
       	}, { offset: '100%' });
	});

	
	/* NIVO SLIDER */
	$('#travelico_slider').each(function(){
		var $this = $(this);
    	$this.nivoSlider({
        	pauseTime: $this.data('pause'),
        	animSpeed: 1000,
        	afterChange: function(){
        		if( $(window).width() > 500 ){
        			$this.find('.nivo-caption .br-caption-holder').css('display', 'block');
        			$this.find('.nivo-caption .br-text-block').each(function(){
	        			var $this = $(this);
        				animate( $this, $this.attr('data-animation_in') );
        			});
        		}
        	},
        	beforeChange: function(){
        		$this.find('.nivo-caption .br-text-block').each(function(){
        			var $this = $(this);
        			animate( $this, $this.attr('data-animation_out'), true );
        		});
        	},
        	afterLoad: function(){
        		if( $(window).width() > 500 ){
        			$this.find('.nivo-caption .br-caption-holder').css('display', 'block');
        			$this.find('.nivo-caption .br-text-block').each(function(){
	        			var $this = $(this);
        				animate( $this, $this.attr('data-animation_in') );
        			});        		
        		}
        	},
        	controlNav: true,
        	prevText: '<i class="fa fa-angle-left"></i>',
        	nextText: '<i class="fa fa-angle-right"></i>',
        });
	});
	
	/* SHORTCODE SLIDER */ 
	$('.slider-shortcode').each(function(){
		var $this = $(this);
		$this.nivoSlider({
			pauseTime: $this.data('interval'),
			controlNavThumbs: $this.data('thumb_nav'),
			manualAdvance: $this.data('autoplay'),
        	prevText: '<i class="fa fa-angle-left"></i>',
        	nextText: '<i class="fa fa-angle-right"></i>',
		})		
	});


	/* ROOM GALLERY SLIDER */
	$('.room-slider').responsiveSlides({
		speed: 800,
		auto: true,
		pager: false,
		nav: true,
		prevText: '<i class="fa fa-chevron-left"></i>',
		nextText: '<i class="fa fa-chevron-right"></i>',
	});	


	/* BUTTON TO TOP */
	//on scolling, show/animate timeline blocks when enter the viewport
	$(window).on('scroll', function(){		
		if( $(window).scrollTop() > 200 ){
			$('.to_top').fadeIn();
		}
		else{
			$('.to_top').fadeOut();
		}
	});
	
	$('.to_top').click(function(e){
		e.preventDefault();
		$("html, body").stop().animate(
			{
				scrollTop: 0
			}, 
			{
				duration: 1200
			}
		);		
	});

	/* NAVIGATION */
	function handle_navigation(){
		if ($(window).width() >= 767) {
			$('ul.nav li.dropdown, ul.nav li.dropdown-submenu').hover(function () {
				$(this).addClass('open').find(' > .dropdown-menu').stop(true, true).hide().slideDown(200);
			}, function () {
				$(this).removeClass('open').find(' > .dropdown-menu').stop(true, true).show().slideUp(200);
	
			});
		}
		else{
			$('ul.nav li.dropdown, ul.nav li.dropdown-submenu').unbind('mouseenter mouseleave');
		}
	}
	handle_navigation();
	
	$(window).resize(function(){
		setTimeout(function(){
			handle_navigation();
		}, 200);
	});	

	/* STICKY NAVIGATION */
	function sticky_nav(){
		var $admin = $('#wpadminbar');
		if( $admin.length > 0 && $admin.css( 'position' ) == 'fixed' ){
			$sticky.css( 'top', $admin.height() );
		}
		else{
			$sticky.css( 'top', '0' );
		}
	}

	var $sticky = $('.sticky_nav');
	if( $sticky.length > 0 ){
		var $top_offset = $('.navigation-bar:first').position().top + $('.navigation-bar:first').height();
		$(window).on('scroll', function(){		
			if( $(window).scrollTop() > $top_offset && $(window).width() > 769 ){
				$sticky.slideDown();
			}
			else{
				$sticky.slideUp();
			}
		});	

		sticky_nav();

		$(window).resize(function(){
			sticky_nav();
		});
	}

	/* UPDATE BUTTONS */
	$('#submit').addClass( 'btn' );

	/* SUBMIT FORMS */
	$('.submit_form').click(function(){
		$(this).parents('form').submit();
	});

	/* REMOVE EXTRA COLUMN FROM VISUAL COMPOSER */ 
	$('.wpb_column').removeClass('wpb_column');
	$('.wpb_text_column').attr( 'class', '');

	/* MAGNIFIC POPUP FOR THE GALLERY */
	$('.gallery').each(function(){
		var $this = $(this);
		$this.magnificPopup({
			type:'image',
			delegate: 'a',
			gallery:{enabled:true},
		});
	});	

	/* CONTACT FORM */
	$('.contact-form a, .send-contact').click(function(){		
		var $this = $(this);
		var $parent = $this.parents( 'form' );
		var $result = $parent.find( '.result' );		
		$.ajax({
			url: ajaxurl,
			data: $parent.serialize(),
			type: 'POST',
			dataType: "JSON",
			success: function( response ){
				if( response.error ){
					$result.html( '<div class="alert alert-danger"><span class="fa fa-times-circle"></span> '+response.error+'</div>' );
				}
				else{
					$result.html( '<div class="alert alert-success"><span class="fa fa-check-circle"></span> '+response.success+'</div>' );
				}
			}
		})
	});

	/* SUBSCRIBE */
	$('.subscribe').click( function(e){
		e.preventDefault();
		var $this = $(this);
		var $parent = $this.parents('.subscribe-form');		
		
		$.ajax({
			url: ajaxurl,
			method: "POST",
			data: {
				action: 'subscribe',
				email: $parent.find( '.email' ).val()
			},
			dataType: "JSON",
			success: function( response ){
				if( !response.error ){
					$parent.find('.sub_result').show().html( '<div class="alert alert-success" role="alert"><span class="fa fa-check-circle"></span> '+response.success+'</div>' );
				}
				else{
					$parent.find( '.sub_result' ).show().html( '<div class="alert alert-danger" role="alert"><span class="fa fa-times-circle"></span> '+response.error+'</div>' );
				}
			}
		})
	} );

	/* ROOMS BOXES HEIGHT */
	function update_sizes(){		
		$('.room-item').each(function(){
			var height = 'auto';
			var $el = $(this).find('.col-sm-2');
			var $el2 = $(this).find('.col-sm-6');
			var line = $(this).find('.vertical-divider');
			if( $(window).width() >= 753 ){
				$el.css( 'height', height );
				$el2.css( 'height', height );
				height = $(this).height();
				line.css( 'height', height );
				line.css( 'right', $el.outerWidth(true) - 10 );
			}
			$el.css( 'height', height );
			$el2.css( 'height', height );
		});
	}
	$(window).load(function(){
		update_sizes();
	});
	
	$(window).resize(function(){
		update_sizes();
	});

	/* DATES RANGE */
	$('.book_date .fa').click(function(){
		var $parent = $(this).parents('.book_date');		
		var $input = $parent.find('input');
		if( $input.length > 0 ){
			if( $input.hasClass('opened') ){
				$input.removeClass('opened');
				$input.datetimepicker('hide');
			}
			else{
				$input.addClass('opened');
				$input.datetimepicker('show');
			}
		}
	});

	$('.book_date select').change(function(){
		$(this).parents('.book_date').find('.fake-select').text( $(this).val() );
	});

	$('.currency-switcher-wrap .fake-select').text( $('option[value="'+$('.currency-switcher-wrap select').val()+'"]').text() );

	$('.book_from').datetimepicker({
		format:'Y-m-d',
		onShow:function( ct ){
			var start = $('.book_to').val();
			var dateMsg = false;
			if( start !== '' ){
				var date = new Date( start );
				date.setDate( date.getDate() - 1 );
				dateMsg = date.getFullYear() +'/'+ (date.getMonth()+1) +'/'+ date.getDate();
			}			
			this.setOptions({
				maxDate: dateMsg
			});
		},
		minDate:'0',
		timepicker:false
	});

	$('.book_to').datetimepicker({
		format:'Y-m-d',
		onShow:function( ct ){
			var start = $('.book_from').val();
			var dateMsg = false;
			if( start !== '' ){
				var date = new Date( start );
				date.setDate( date.getDate() );
				dateMsg = date.getFullYear() +'/'+ (date.getMonth()+1) +'/'+ date.getDate();
			}
			
			this.setOptions({
				minDate: dateMsg
			});
		},
		timepicker:false
	});
	
	$('.bookdate').datetimepicker({
		format:'Y-m-d',
		minDate:'0',
		timepicker:false
	});
	
	$(".digitonly").keypress(function (e) {
     //if the letter is not digit then display error and don't type anything
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        //display error message
        $("#errmsg").html("Digits Only").show().fadeOut("slow");
               return false;
    }
   });
   
	/* UPDATE PRICES */
	var nights = 0;
	if( $('.book_from').val() !== '' && $('.book_to').val() !== '' ){
		var a = new Date( $('.book_from').val() );
		var b = new Date( $('.book_to').val() );

		var utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
		var utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());

		nights = Math.floor( (utc2 - utc1) / ( 1000 * 60 * 60 * 24 ) );
	}

	$('.room-item').each(function(){
		var $this = $(this);
		var $select = $this.find('select');

		var $price_holder = $this.find('.price_holder');
		var price_precision = $price_holder.data('price_precision');
		var thousands_separator = $price_holder.data('thousands_separator');
		var decimal_separator = $price_holder.data('decimal_separator');
		var currency_symbol = $price_holder.data('currency_symbol');
		var currency_symbol_pos = $price_holder.data('currency_symbol_pos');
		
		var price = $this.find('.price-calc').text();

		var re = new RegExp( thousands_separator, 'g');
		var check_price = price.replace( re, '' );
		if( check_price == '' ){
			price = price.replace( thousands_separator, '' );
		}
		else{
			price = check_price;
		}

		price = price.replace( decimal_separator, '.' );		

		price = price.replace( currency_symbol, '' );		

		$select.change(function(){
			var val = $(this).val();
			var value = val * price * nights;

			if( val == 0 ){
				$price_holder.fadeOut( 200 );
			}
			else{
				$price_holder.find('h5').html( value );
				$price_holder.fadeIn( 200 );

				$price_holder.find('h5').formatCurrency({
					positiveFormat: currency_symbol_pos == 'front' ? '%s%n' : '%n%s',
					symbol: currency_symbol,
					decimalSymbol: decimal_separator,
					digitGroupSymbol: thousands_separator,
					roundToDecimalPlace: price_precision
				});				
			}
		});		
	});

	$('.room-book-holder .book_date select').change();

	/* BOOK SELECTED ROOMS */
	var $booking_form = $('.booking_form');
	$booking_form.html( $('.search_form').html() );
	$booking_form.append( '<input type="hidden" value="'+nights+'" name="nights">' );
	var room_id_count = '';
	$('.room-book').click(function(){
		$('.room-item').each(function(){
			var $this = $(this)
			if( $this.is(':visible') && $this.find('select').val() > 0 ){
				room_id_count += '<input type="hidden" name="room_id_count[]" value="'+( $this.find('select').attr('name').split('room_type_')[1]+'-'+$this.find('select').val() )+'">';
			}
		});

		if( room_id_count !== '' ){
			$booking_form.append( room_id_count );
			$booking_form.submit();
		}
	});

	$('.book-finish, .book-cancel').click(function(){
		var $this = $(this);
		var $form = $this.parents('form');
		$form.find( 'small.error' ).remove();
		var can_submit = true;

		$form.find('input, textarea').each(function(){
			var $$this = $(this);			
			$$this.removeClass( 'error' )
			var valid = true;
			if( $$this.hasAttr('data-validation') ){
				var validations = $$this.data('validation').split('|');
				for( var i=0; i<validations.length; i++ ){
					switch ( validations[i] ){
						case 'required' : 
							if( $$this.val() == '' ){
								valid = false;
							} break;
						case 'number' : 
							if( isNaN( parseInt( $$this.val() ) ) ){
								valid = false;
							} break;
						case 'email' : 
							if( !/\S+@\S+\.\S+/.test( $$this.val() ) ){
								valid = false
							} break;
					}
				}
			}

			if( !valid ){
				can_submit = false;
				$$this.addClass('error');
				$$this.before('<small class="error">'+$$this.data('error')+'</small>');
			}
		});

		if( can_submit ){
			$form.submit();
		}
	});

	/* UPDATE CURRENCY */
	$('.change-currency').change(function(){
		var $this = $(this);
		$this.parents('.book_date').find('.fake-select').text( $this.find('option[value="'+$this.val()+'"]').text() );
		$.ajax({
			url: ajaxurl,
			data: {
				action: 'update_currency',
				currency_id: $this.val()
			},
			type: 'POST',
			complete: function(){
				window.location.reload();
			}
		})
	});

	/* UPDATE BOOKING FORM ON HOME SLIDER */
	function slider_booking_classes(){
		if( $(window).width() > 768 ){
			$('.home-slider .container').removeClass('container').addClass('container-tr');
			$('.home-slider .row').removeClass('row').addClass('row-tr');
			$('.home-slider .col-sm-5').removeClass('col-sm-5').addClass('col-sm-5-tr');
			$('.home-slider .col-sm-2').removeClass('col-sm-2').addClass('col-sm-2-tr');
		}
		else{
			$('.home-slider .container-tr').removeClass('container-tr').addClass('container');
			$('.home-slider .row-tr').removeClass('row-tr').addClass('row');
			$('.home-slider .col-sm-5-tr').removeClass('col-sm-5-tr').addClass('col-sm-5');
			$('.home-slider .col-sm-2-tr').removeClass('col-sm-2-tr').addClass('col-sm-2');
		}
	}
	slider_booking_classes();
	$(window).resize(function(){
		slider_booking_classes();
	});

	/* SCALE FONT SIZES */
	function scale_slider_fonts(){
		$('.br-text-block strong, .br-text-block span,.br-text-block h1, .br-text-block h2, .br-text-block h3, .br-text-block h4, .br-text-block h5, .br-text-block h6, .br-text-block p, .br-text-block a').each(function(){
			var $this = $(this);
			var in_font_size = $this.data('in_font_size');
			var in_line_height = $this.data('in_line_height');

			var in_padding_top = $this.data('in_padding_top');
			var in_padding_left = $this.data('in_padding_left');
			var in_padding_right = $this.data('in_padding_right');
			var in_padding_bottom = $this.data('in_padding_bottom');
			
			var in_margin_top = $this.data('in_margin_top');
			var in_margin_left = $this.data('in_margin_left');
			var in_margin_bottom = $this.data('in_margin_bottom');
			var in_margin_right = $this.data('in_margin_right');	

			if( typeof in_font_size == 'undefined' ){
				in_font_size = $this.css('font-size');
				in_line_height = $this.css('line-height');

				in_padding_top = $this.css('padding-top');
				in_padding_left = $this.css('padding-left');
				in_padding_bottom = $this.css('padding-bottom');
				in_padding_right = $this.css('padding-right');
				in_margin_top = $this.css('margin-top');

				in_margin_left = $this.css('margin-left');
				in_margin_bottom = $this.css('margin-bottom');
				in_margin_right = $this.css('margin-right');				

				$this.data('in_font_size', in_font_size);
				$this.data('in_line_height', in_line_height);

				$this.data('in_padding_top', in_padding_top);
				$this.data('in_padding_left', in_padding_left);
				$this.data('in_padding_bottom', in_padding_bottom);
				$this.data('in_padding_right', in_padding_right);
				
				$this.data('in_margin_top', in_margin_top);
				$this.data('in_margin_left', in_margin_left);
				$this.data('in_margin_bottom', in_margin_bottom);
				$this.data('in_margin_right', in_margin_right);				
			}

			var new_font_size = parseFloat( in_font_size );
			var new_line_height = parseFloat( in_line_height );

			var new_padding_top = parseFloat( in_padding_top );
			var new_padding_left = parseFloat( in_padding_left );
			var new_padding_bottom = parseFloat( in_padding_bottom );
			var new_padding_right = parseFloat( in_padding_right );
			
			var new_margin_top = parseFloat( in_margin_top );
			var new_margin_left = parseFloat( in_margin_left );
			var new_margin_bottom = parseFloat( in_margin_bottom );
			var new_margin_right = parseFloat( in_margin_right );			
			var rate =  $(window).width() / 1024;
			if( $(window).width() < 1024 ){
				new_font_size = parseFloat( new_font_size ) * rate;
				new_line_height = parseFloat( new_line_height ) * rate;

				new_padding_top = parseFloat( new_padding_top ) * rate;
				new_padding_left = parseFloat( new_padding_left ) * rate;
				new_padding_bottom = parseFloat( new_padding_bottom ) * rate;
				new_padding_right = parseFloat( new_padding_right ) * rate;
				
				new_margin_top = parseFloat( new_margin_top ) * rate;
				new_margin_left = parseFloat( new_margin_left ) * rate;
				new_margin_bottom = parseFloat( new_margin_bottom ) * rate;
				new_margin_right = parseFloat( new_margin_right ) * rate;				
			}

			$this.css( 'font-size', new_font_size+'px' );
			$this.css( 'line-height', new_line_height+'px' );

			$this.css( 'padding-top', new_padding_top+'px' );
			$this.css( 'padding-left', new_padding_left+'px' );
			$this.css( 'padding-bottom', new_padding_bottom+'px' );
			$this.css( 'padding-right', new_padding_right+'px' );
			
			$this.css( 'margin-top', new_margin_top+'px' );
			$this.css( 'margin-left', new_margin_left+'px' );
			$this.css( 'margin-bottom', new_margin_bottom+'px' );
			$this.css( 'margin-right', new_margin_right+'px' );			
		})
	}
	scale_slider_fonts();
	$(window).resize(function(){
		setTimeout(function(){
			scale_slider_fonts();
		}, 500);
	});

	/* ASSIGN ADULTS AND KIDS */
	var adults = $('select[name="adults"]').val();
	var kids = $('select[name="kids"]').val();
	$('.room-book-holder select').change(function(){
		var $this = $(this);
		var old_val = $this.data('old_val');
		var val = parseInt( $this.val() );
		var $room_box = $this.parents('.room-item');

		var max_adults = 0;
		if( $room_box.find('.max_adults').length > 0 ){
			max_adults = parseInt( $room_box.find('.max_adults').text() );
		}

		var max_kids = 0;
		if( $room_box.find('.max_kids').length > 0 ){
			max_kids = parseInt( $room_box.find('.max_kids').text() );
		}

		adults -= max_adults * val;
		kids -= max_kids * val;

		adults += max_adults * old_val;
		kids += max_kids * old_val;

		$this.data( 'old_val', val );

		var $adults = $('.assign-info .adults');
		$adults.text( adults < 0 ? 0 : adults );
		$adults.parents('span').removeClass('red green');
		if( adults > 0 ){
			$adults.parents('span').addClass( 'red' );
		}
		else{
			$adults.parents('span').addClass( 'green' );
		}
		
		var $kids = $('.assign-info .kids');
		$kids.text( kids < 0 ? 0 : kids );
		$kids.parents('span').removeClass('red green');

		if( kids > 0 ){
			$kids.parents('span').addClass( 'red' );
		}
		else{
			$kids.parents('span').addClass( 'green' );
		}		

	});
	/* END ASSIGN ADULTS AND KIDS */

	/* ASSIGN ACTIVE FOR TABS */
	$('.book-search-tab').click(function(){
		$('.book-search-tab.active').removeClass('active');
		$(this).addClass('active');
	});
	
	$("#subscribenow").click(function()
       {
		   if($('#nname').val() == ''){
			alert('Please enter your name');
			$('#nname').focus();
			return false;
			}
			if($('#nemail').val() == ''){
			alert('Please enter your email');
			$('#nemail').focus();
			return false;
			}
			if(!isEmail($('#nemail').val())){
			alert('Please enter valid email');
			$('#nemail').focus();
			return false;
			}
			if($('#nmobile').val() == ''){
			alert('Please enter Mobile Number');
			$('#nmobile').focus();
			return false;
			}
			
			
               var nname = $('#nname').val();
			   var nmobile = $('#nmobile').val();
			   var nemail = $('#nemail').val();
                       $.ajax({
                          type: "POST",
                          url: "include/function.php",
                          data: "&name="+nname+"&email="+nemail+"&mobile="+nmobile+"&action=nsubscribe",
                          cache: false,
						  beforeSend: function() { 
							  $("#subscribenow").html('Sending...');
							},
                          success: function(){
                         $('#nresult').html('<span style="color:#fff;text-align:center;">Thank you for subscription, you shall receive regular travel updates from 99DESTINATIONS.</span>');
						 $('#nemail').val('');
						 $('#nname').val('');
						 $('#nmobile').val('')
						 $("#subscribenow").html('SUBSCRIBE NOW');
                         }
                        });
       return false;
       });
	
	function isEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}
});