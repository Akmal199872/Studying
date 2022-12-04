<?php
	$skills = [
      [
      	'name' => 'adobe',
        'value' => 22
      ],
      [
      	'name' => 'photo',
        'value' => 77
      ],
      [
      	'name' => 'media',
        'value' => 11
      ]
    ];
    
    echo "<pre>";
    //foreach ($skills as $skill) {
    	//print_r($skill);
    //    echo "<br>";
    //	echo $skill['name']. " значение ".$skill['value']. "<br>";
    //}
    foreach ($skills as $key => $skill): ?>

    <?php if ($key == 0):?> current <?php endif ?>
    

<?=$skill['name'] ?> <?=$skill['value']?>
<?php endforeach;?>