<?php
	$cart = [
    	'name' => 'Кофемолка',
        'price' => 234
    ];
    echo "<pre>";
    //print_r($cart['price']);
    print_r($cart);
    
    
    $cart2 = [
    	[
          'name' => 'Кофемолка',
          'price' => 234
        ],
        [
          'name' => 'Чайник',
          'price' => 35        	
        ]
    ];
    
	echo "<pre>";
	print_r($cart2);
    
	echo "<pre>";
	print_r($cart2[1]['price']);
?>