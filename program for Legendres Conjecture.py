Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def isprime( n ):
...     i = 2
...     for i in range(2, int((math.sqrt(n)+1))):
...         if n%i == 0:
...             return False
...     return True
... 
>>> def LegendreConjecture( n ):
...     print("Primes in the range ", n*n, " and ", (n+1)*(n+1), " are: ")
...     for i in range(n*n, (((n+1)*(n+1))+1)):
...         print(i)
... 
...         
>>> n = 50
>>> LegendreConjecture(n)
Primes in the range  2500  and  2601  are: 
2500
2501
2502
2503
2504
2505
2506
2507
2508
2509
2510
2511
2512
2513
2514
2515
2516
2517
2518
2519
2520
2521
2522
2523
2524
2525
2526
2527
2528
2529
2530
2531
2532
2533
2534
2535
2536
2537
2538
2539
2540
2541
2542
2543
2544
2545
2546
2547
2548
2549
2550
2551
2552
2553
2554
2555
2556
2557
2558
2559
2560
2561
2562
2563
2564
2565
2566
2567
2568
2569
2570
2571
2572
2573
2574
2575
2576
2577
2578
2579
2580
2581
2582
2583
2584
2585
2586
2587
2588
2589
2590
2591
2592
2593
2594
2595
2596
2597
2598
2599
2600
2601
