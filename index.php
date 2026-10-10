<?php
header('Content-Type: application/json');
echo json_encode(['branch' => 'lang/php', 'lang' => 'php', 'path' => $_SERVER['REQUEST_URI'] ?? '/']);
