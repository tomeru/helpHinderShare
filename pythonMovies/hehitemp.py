    %% scenario number 1: Strong wants cherrry, weak wants cheese, no amb

      paths_s = [1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;... 
                 1 1 2 3 4 5 6 6 6 6 6 6 6 6 6 6 ];

      paths_w = [7 7 7 6 6 6 6 6 6 6 6 6 6 6 6 6 ;... 
                 1 1 1 1 2 3 3 3 4 4 5 6 6 6 6 6 ];

      actions_s = [3 5 5 5 5 5 1 1 1 1 1 1 1 1 1 ];

      actions_w = [5 2 2 5 5 5 5 5 5 5 5 1 1 1 1 ];
      
      best_k = [3 4 6];


      %% scenario number 2: Strong wants cheese, weak wants cherry. Amb between hinder and two goals
   case 2
      paths_s = [1 1 2 3 4 5 6 6 6 6 6 6 6 6 6 6 ;... 
                 1 2 2 2 2 2 2 3 4 5 6 6 6 6 6 6 ];

      paths_w = [7 7 7 6 6 6 7 6 5 5 4 3 3 2 2 2 ;... 
                 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 4 ];

      actions_s = [5 3 3 3 3 3 5 5 5 5 1 1 1 1 1 ];

      actions_w = [5 2 2 5 2 2 2 2 2 2 2 2 2 5 5 ];
      
      best_k = [4 7 8];

   case 3
      %% scenario number 3: Strong and weak want cherry, weak gets there first, strong pushes weak off cherry

      paths_s = [1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;... 
                 1 2 2 3 4 5 6 6 6 6 6 6 6 6 6 6 ];

      paths_w = [1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;...         
                 7 7 7 7 6 6 7 7 7 7 7 7 7 7 7 7 ];

      actions_s = [5 3 5 5 5 5 1 1 1 1 1 1 1 1 1  ];

      actions_w = [3 4 4 4 1 1 4 4 4 4 4 4 4 4 4  ];
      
      best_k = [3 6 8];

   case 4
      %% scenario number 4: Strong and weak want cherry, strong gets there first, weak feebly tries to get on it

      paths_s = [1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;... 
                 1 1 2 3 4 5 6 6 6 6 6 6 6 6 6 6 ];

      paths_w = [6 6 6 5 5 5 4 4 3 3 3 3 3 3 3 3 ;...
                 4 4 5 5 6 6 6 6 6 6 6 6 6 6 6 6 ];


      actions_s = [3 5 5 5 5 5 1 1 1 1 1 1 1 1 1 ];

      actions_w = [5 5 2 5 2 2 2 2 2 2 2 2 2 2 2 ];
      
      best_k = [3 7 8];
      
   case 5
      %% scenario number 5: Strong wants to get to cheese and happens to push weak onto the cherry, its goal

      paths_s = [1 1 2 2 2 2 3 3 4 5 6 6 6 6 6 6 ;...
                 1 2 2 3 4 5 5 6 6 6 6 6 6 6 6 6 ]; 

      paths_w = [2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;...         
                 4 4 4 5 5 6 6 6 6 6 6 6 6 6 6 6 ];

      actions_s = [5 3 5 5 5 3 5 3 3 3 1 1 1 1 1 ];

      actions_w = [5 5 5 5 5 1 1 1 1 1 1 1 1 1 1 ];
      
      best_k = [5 6 8];
   
   case 6
          % Scenario 6:

      % S comes from top right to hinder W, blocking at 24 W comes from 11. 

      paths_s =   [7 7 6 5 4 3 2 2 2 2 2 2 2 2 2 2 ; 
                   7 6 6 6 6 6 6 5 4 4 4 4 4 4 4 4 ];

      paths_w =   [1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
                   1 1 1 1 1 2 2 3 3 3 3 3 3 3 3 3 ];

      actions_s =  [4 2 2 2 2 2 4 4 1 1 1 1 1 1 1 ];
      
      actions_w =  [3 3 5 5 5 5 5 5 5 5 5 5 5 5 5  ];
      
      best_k = [4 7 8];
      

   case 7
      % Scenario 7:

      % S comes long way to help W

      paths_s =   [6 6 6 5 4 3 3 2 2 2 2 2 2 2 2 2 ; 
                   4 3 2 2 2 2 1 1 2 3 4 5 5 5 5 5 ];

      paths_w =   [1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
                   1 1 1 1 1 2 2 2 3 4 5 6 6 6 6 6 ];
               
      actions_s =  [4 4 2 2 2 4 2 5 5 5 5 1 1 1 1 ];
      
      actions_w =  [3 3 5 5 5 5 5 5 5 5 5 1 1 1 1 ];
      
      best_k = [3 6 7];

   case 8
      %% scenario number 8: Strong gets out of the way to help weak get to cheese

      paths_s = [6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 ;...
                 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ];

      paths_w = [6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 ;...
                 2 3 4 4 5 5 6 6 6 6 6 6 6 6 6 6 ];


      actions_s = [5 3 1 1 1 1 1 1 1 1 1 1 1 1 1 ];

      actions_w = [5 5 5 5 5 5 1 1 1 1 1 1 1 1 1];

      best_k = [3 4 5];
      
   case 9
      % Scenario 9:
      % S pushes W to its goal in order to set up a hinder push 

      paths_s =   [ 7 7 6 5 4 3 3 2 2 2 2 2 2 2 2 2 ;
                    7 6 6 6 6 6 7 7 6 5 4 3 2 2 2 2 ];   

      paths_w =   [ 5 5 4 4 3 2 2 2 2 2 2 2 2 2 2 2 ;
                    6 6 6 6 6 6 6 6 5 4 3 2 1 1 1 1 ];

      actions_s =   [ 4 2 2 2 2 5 2 4 4 4 4 4 1 1 1 ];

      actions_w =   [ 2 2 2 2 2 1 1 1 5 5 5 5 5 5 5 ];
      
      best_k = [4 6 8];
      
   case 10
      % Scenario 10:
      % S moves to block cherry door, moving across cherry

      paths_s =   [ 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
                    7 7 6 5 4 4 4 4 4 4 4 4 4 4 4 4 ];

      paths_w =   [ 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
                    1 1 1 2 2 3 3 3 3 3 3 3 3 3 3 3 ];

      actions_s =   [ 3 4 4 4 1 1 1 1 1 1 1 1 1 1 1 ];

      actions_w =   [ 3 3 5 5 5 5 5 5 5 5 5 5 5 5 5 ];
      
      best_k = [3 4 5]
      
   case 11
      % Scenario 11:
      % S pushes W onto cheese to set up a push onto the cherry

      paths_s =   [ 7 6 6 6 6 6 7 7 6 5 4 3 3 3 3 3 ; 
                    1 1 2 3 4 5 5 6 6 6 6 6 6 6 6 6 ];

      paths_w =   [ 6 6 6 6 6 6 5 5 4 4 3 2 2 2 2 2 ;
                    4 4 4 5 5 6 6 6 6 6 6 6 6 6 6 6 ];

      actions_s =   [ 2 5 5 5 5 3 5 2 2 2 2 1 1 1 1 ];

      actions_w =   [ 5 5 5 5 1 2 2 2 2 2 2 1 1 1 1 ];
      
      best_k = [3 7 8];

   case 12
      % Scenario 12:
      % flip case of 2 resolves to hinder

      paths_s =   [ 1 1 2 3 4 5 6 6 6 5 5 5 5 5 6 6 ; 
                    1 2 2 2 2 2 2 3 2 2 2 2 2 2 2 2 ];  

      paths_w =   [ 7 7 7 6 5 6 7 6 6 5 5 5 5 6 6 6 ; 
                    1 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 ];

      actions_s =   [ 5 3 3 3 3 3 5 4 2 1 1 1 1 3 1 ]; 

      actions_w =   [ 5 2 2 2 2 2 2 5 2 5 5 5 3 5 5 ];
    
      best_k = [3 5 8];
      
      
   case 13

%% sc 1 with idle boulder: Strong wants cherrry, weak wants cheese, no amb

      paths_s = [1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;... 
                 1 1 2 3 4 5 6 6 6 6 6 6 6 6 6 6 ];

      paths_w = [7 7 7 6 6 6 6 6 6 6 6 6 6 6 6 6 ;... 
                 1 1 1 1 2 3 3 3 4 4 5 6 6 6 6 6 ];
               
      paths_b = [3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 ;... 
                 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ];

      actions_s = [3 5 5 5 5 5 1 1 1 1 1 1 1 1 1 ];

      actions_w = [5 2 2 5 5 5 5 5 5 5 5 1 1 1 1 ];
      
      best_k = [3 5 7];
      
      
   case 14
      %% sc 4 with idle boulder: Strong and weak want cherry, strong gets there first, weak feebly tries to get on it

      paths_s = [1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;... 
                 1 1 2 3 4 5 6 6 6 6 6 6 6 6 6 6 ];

      paths_w = [6 6 6 5 5 5 4 4 3 3 3 3 3 3 3 3 ;...
                 4 4 5 5 6 6 6 6 6 6 6 6 6 6 6 6 ];

      paths_b = [3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 ;... 
                 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ];
               
      actions_s = [3 5 5 5 5 5 1 1 1 1 1 1 1 1 1 ];

      actions_w = [5 5 2 5 2 2 2 2 2 2 2 2 2 2 2 ];
      
      best_k = [3 5 7];
      
      
   case 15
      % Sc 7 with idle boulder

      % S comes long way to help W

      paths_s =   [6 6 6 5 4 3 3 2 2 2 2 2 2 2 2 2 ; 
                   4 3 2 2 2 2 1 1 2 3 4 5 5 5 5 5 ];

      paths_w =   [1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2  ;
                   1 1 1 1 1 2 2 2 3 4 5 6 6 6 6 6  ];
                 
      paths_b =   [5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ;... 
                   6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 ];
               
      actions_s =  [4 4 2 2 2 4 2 5 5 5 5 1 1 1 1 ];
      
      actions_w =  [3 3 5 5 5 5 5 5 5 5 5 1 1 1 1 ];

      best_k = [4 6 7];
      
   case 16
      
      % boulder1_boulder 
      %strong and weak start in bottom-left, with boulder blocking top-left. strong pushes boulder beyond left-goal.


      paths_s =  [2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3; 
                  2 3 4 5 6 6 6 6 6 6 6 6 6 6 6 6];

      actions_s = [5 5 5 5 3 1 1 1 1 1 1 1 1 1 1];

      paths_w = [3 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2;
                 2 2 2 2 3 4 4 5 6 6 6 6 6 6 6 6];

      actions_w =[2 2 5 5 5 5 5 5 1 1 1 1 1 1 1];


      paths_b = [2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2;
                 4 4 5 6 7 7 7 7 7 7 7 7 7 7 7 7];


    case 17
      % Boulder hinder II
      % Boulder gets pushed onto cherries. Strong retires to avoid accidentally nudging boulder.


      paths_s = [6 6 5 4 3 3 3 3 3 3 3 3 3 3 3; 
                 5 6 6 6 6 7 7 7 7 7 7 7 7 7 7];

      actions_s = [5 2 2 2 5 1 1 1 1 1 1 1 1 1];


      paths_w = [2 2 2 2 2 2 2 2 2 2 2 2 2 2 2; 
                 2 2 3 3 4 5 5 5 5 5 5 5 5 5 5];

      actions_w = [5 5 5 5 5 1 1 1 1 1 1 1 1];


      paths_b = [5 5 4 3 2 2 2 2 2 2 2 2 2 2 2;
                 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6];

    case 18
      % variant: boulder blocks W's entrance and weak reverts to other entrance. needs to be extended


      paths_s =[6 6 5 4 3 3 2 2 2 2 2 2 2 2 2; 
                5 6 6 6 6 7 7 6 6 6 6 6 6 6 6];

      actions_s =[5 2 2 2 5 2 4 4 1 1 1 1 1 1];


      paths_w = [2 2 2 2 2 2 2 2 2 2 2 3 3 4 4; 
                 2 2 3 3 4 4 3 3 3 2 2 2 2 2 2];

      actions_w =[5 5 5 5 5 4 4 4 4 3 3 3 3];


      paths_b = [5 5 4 3 2 2 2 2 2 2 2 2 2 2 2;
                 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5];

    case 19
    % the above can be adapted to a locking-in hinder case in which 4,2 is blocked. another possibility is % just to have a second boulder in 4,2

    % assuming naming is the same the same it would look as follows

    paths_s = [6 6 5 4 3 3 2 2 2 2 2 2 2 2 2; 
               5 6 6 6 6 7 7 6 5 5 5 5 5 5 5];

    actions_s = [5 2 2 2 5 2 4 4 4 1 1 1 1 1];


    paths_w = [2 2 2 2 2 2 2 2 2 2 2 2 2 2 2; 
               1 1 2 2 2 3 3 3 3 3 3 3 3 3 3];

    actions_w = [5 5 5 5 5 5 5 5 1 1 1 1 1];


    paths_b = [5 5 4 3 2 2 2 2 2 2 2 2 2 2 2;
               6 6 6 6 6 6 5 4 4 4 4 4 4 4 4];

    % paths_b2= [4 4 4 4 4 4 4 4 4 4 4 4 4 4 4;
    % 	     2 2 2 2 2 2 2 2 2 2 2 2 2 2 2];

    case 20

    % Boulder-Help---trapped in by boulders on bottom level (pushing)


    paths_s = [1 2 3 3 2 2 2 2 2 2 2 2 2 2 2; 
               1 1 1 2 2 1 1 2 3 4 5 5 5 5 5];

    actions_s = [3 3 5 2 4 1 5 5 5 5 1 1 1 1];


    paths_w = [4 4 4 4 4 3 2 2 2 2 2 2 2 2 2; 
               2 2 2 2 2 2 2 3 4 5 6 6 6 6 6];

    actions_w = [3 3 3 3 3 3 5 5 5 5 1 1 1];


    paths_b = [3 3 3 3 3 3 3 3 3 3 3 3 3 3 3;
               2 2 2 3 3 3 3 3 3 3 3 3 3 3 3];

%     paths_b2 = [5 5 5 5 5 5 5 5 5 5 5 5 5 5 5;
%                 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2];


    case 21
    % Boulder-Help---trapped in by boulders on top level (no pushing)


    paths_s = [1 2 3 3 3 3 3 3 3 3 3 3 3 3 3; 
               7 7 7 6 7 7 7 7 7 7 7 7 7 7 7];

    actions_s = [3 3 4 5 1 1 1 1 1 1 1 1 1 1];


    paths_w = [4 4 4 4 4 3 3 2 2 2 2 2 2 2 2; 
               6 6 6 6 6 6 6 5 5 5 5 5 5 5 5];

    actions_w = [3 3 3 3 3 3 3 1 1 1 1 1 1 1];


    paths_b = [3 3 3 3 3 3 3 3 3 3 3 3 3 3 3;
               6 6 6 5 5 5 5 5 5 5 5 5 5 5 5];

%     paths_b2= [5 5 5 5 5 5 5 5 5 5 5 5 5 5 5;
%            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6];



    case 22
    % boulder selfish
    %strong starts in bottom right and weak in bottom left. Boulder at 2,4
    % strong pushes boulder up and then rests on left goal (also W's goal).


    paths_s = [5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
               2 2 2 2 3 4 5 6 6 6 6 6 6 6 6 6];

    actions_s = [2 2 2 5 5 5 5 1 1 1 1 1 1 1 1 1];

    paths_w = [1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2;
               1 1 1 1 1 2 3 3 4 5 5 5 5 5 5 5];

    actions_w = [3 3 5 5 5 5 5 1 1 1 1 1 1 1 1];


    paths_b = [2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2;
               4 4 4 4 4 5 6 7 7 7 7 7 7 7 7 7];

    case 23
    % boulder selfish 2
    %strong starts in bottom right and weak in bottom left. Boulder at 2,4
    % strong pushes boulder up and then rests on left goal. W goes off to his goal.

    paths_s= [5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
               2 2 2 2 3 4 5 6 6 6 6 6 6 6 6 6];

    actions_s = [2 2 2 5 5 5 5 1 1 1 1 1 1 1 1 ];
 
    paths_w = [1 1 2 2 2 2 2 2 2 2 2 3 3 4 5 5;
              1 1 1 1 1 2 3 3 4 5 5 5 6 6 6 6];

    actions_w = [3 3 5 5 5 5 5 5 5 3 3 5 3 3 3 ];


    paths_b = [2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2;
               4 4 4 4 4 5 6 7 7 7 7 7 7 7 7 7];



    case 24
    % boulder tricky help
    % S is a helper and starts in top-right near W's goal. Boulder is in 6,4.
    % S pushes boulder down and then pushes W up to goal.

    paths_s =  [7 6 6 6 6 6 7 7 6 6 6 6 6 6 6 6;
               6 6 5 4 3 2 2 1 1 2 3 4 5 5 5 5];

    actions_s = [2 4 4 4 4 3 4 2 5 5 5 5 1 1 1];

    paths_w=  [5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6;
               3 3 3 2 2 2 2 3 4 5 6 6 6 6 6 6];

    actions_w = [4 4 4 2 2 2 3 5 5 5 5 1 1 1 1];

    paths_b =  [6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5;
                4 4 4 3 2 1 1 1 1 1 1 1 1 1 1 1];

    case 25
    % boulder sadistic imprisonment
    % S is a helper and starts in top-right near W's goal. Boulder is in 6,4.
    % S pushes boulder down and then locks W into corner


    paths_s=  [7 6 6 6 6 6 6 5 5 6 6 7 7 7 7 7;
               6 6 5 4 3 2 3 3 2 2 3 3 2 2 2 2];

    actions_s = [2 4 4 4 4 5 2 4 3 5 3 4 1 1 1];

    paths_w=  [5 5 5 5 5 5 6 6 6 7 7 7 7 7 7 7;
               3 3 3 2 2 2 2 2 2 2 2 2 1 1 1 1];

    actions_w = [4 4 4 2 2 2 3 4 4 4 2 2 5 5 5];

    paths_b =  [6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6;
                4 4 4 3 2 1 1 1 1 1 1 1 1 1 1 1];
 
      
      
    case 101
        % Training 1:
        % Strong moves more easily than weak

        
        paths_s = [ 1 2 3 3 4 5 5 5 5 5 5 5 5 5 5 5 5 ;
                    5 5 5 6 6 6 7 7 7 7 7 7 7 7 7 7 7 ];
         
        paths_w = [ 1 1 1 1 1 1 1 1 2 2 3 3 3 4 5 5 5 ;
                    1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 3 ];
                  
        actions_s = [ 3 3 5 3 3 5 1 1 1 1 1 1 1 1 1 1 ];

        actions_w = [ 1 1 1 1 1 1 3 3 3 3 5 3 3 3 5 5 ];

   
    case 102
        % Training 3:
        % Strong can push weak, but not vice versa

        paths_s = [ 2 2 2 3 4 4 4 4 4;
                    4 3 2 2 2 2 2 2 2];

        paths_w = [ 3 3 3 4 5 5 5 5 5;
                    1 1 2 2 2 2 2 2 2];

        actions_s = [ 4 4 3 3 1 1 1 1];

        actions_w = [ 5 5 1 1 2 2 2 2];
        
    case 103
      % Training 4:
      % Strong can push boulders. Weak can't

      paths_s =  [ 1 1 2 3 4 5 5 6 6 6 6 6 6 6 6; 
                   1 2 2 2 2 2 1 1 2 3 2 1 1 1 1];

      actions_s =  [ 5 3 3 3 3 4 3 5 5 4 4 1 1 1];


      paths_w =  [ 7 7 7 7 7 7 7 7 7 7 6 6 6 6 6; 
                   5 5 5 5 5 5 5 5 5 5 5 5 5 5 5];

      actions_w =  [ 1 1 1 1 1 1 1 1 2 2 4 4 4 4];


      paths_b =   [2 2 3 4 5 6 6 6 6 6 6 6 6 6 6;
                   2 2 2 2 2 2 2 2 3 4 4 4 4 4 4];

    case 104
      % Training 4:
      % Small and weak doing stuff

      paths_s = [ 3 2 2 2 2 2 2 2 ;
                  1 1 2 3 4 5 6 6 ];

      paths_w = [ 5 5 6 6 6 6 6 6 ;
                  3 3 3 4 4 5 5 6 ];

      actions_s = [ 2 5 5 5 5 5 1];

      actions_w = [ 3 3 5 5 5 5 5];
        
    case 201
      % Selfish basic
      paths_s = [1 1 2 3 4 5 6 6 6 6 6 6 6 6 6 6 ;... 
                 1 2 2 2 2 2 2 3 4 5 6 6 6 6 6 6 ];

      paths_w = [7 7 7 6 6 6 7 6 5 5 4 3 3 2 2 2 ;... 
                 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 4 ];

      actions_s = [5 3 3 3 3 3 5 5 5 5 1 1 1 1 1 ];

      actions_w = [5 2 2 5 2 2 2 2 2 2 2 2 2 5 5 ];
      
      best_k = [4 7 8];
      
    case 202
      % Helping basic
      
      paths_s =   [6 6 6 5 4 3 3 2 2 2 2 2 2 2 2 2 ; 
                   4 3 2 2 2 2 1 1 2 3 4 5 5 5 5 5 ];

      paths_w =   [1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
                   1 1 1 1 1 2 2 2 3 4 5 6 6 6 6 6 ];
               
      actions_s =  [4 4 2 2 2 4 2 5 5 5 5 1 1 1 1 ];
      
      actions_w =  [3 3 5 5 5 5 5 5 5 5 5 1 1 1 1 ];
      
      best_k = [3 6 7];
      
    case 203
      % Hinder basic
      
      paths_s =   [7 7 6 5 4 3 2 2 2 2 2 2 2 2 2 2 ; 
                   7 6 6 6 6 6 6 5 4 4 4 4 4 4 4 4 ];

      paths_w =   [1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ;
                   1 1 1 1 1 2 2 3 3 3 3 3 3 3 3 3 ];

      actions_s =  [4 2 2 2 2 2 4 4 1 1 1 1 1 1 1 ];
      
      actions_w =  [3 3 5 5 5 5 5 5 5 5 5 5 5 5 5  ];
      
      best_k = [4 7 8];