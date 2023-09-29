// code for solution to game
function randomQueen(n) {
    var nsq = n*n;
    return Math.floor(Math.random() * nsq) % n;
  }
  
  // cc == window.chessController
  function placeInitialQueens(arrBoard) {
    var n = arrBoard.length;
  
    for (var rowN = 0; rowN < n; rowN++) {
      var column = randomQueen(n);
  
      arrBoard[rowN][column] = 1;
    }
  }
  
  function findMostThreatenedQueen(arrBoard) {
    var n = arrBoard.length;
  
    var q = -1;
    var maxThreats = -1;
  
    for (var row = 0; row < n; row++) {
      for (var col = 0; col < n; col++) {
        if (arrBoard[row][col] != 1) {
          continue;
        }
        // console.log("row,col",row,col);
        var t = findNumberOfThreats(arrBoard, row, col);
        // console.log("threats",t);
        if (t > maxThreats) {
          q = [row,col];
          maxThreats = t;

        }
        // break; // move to next row
      }
    }
    if(maxThreats==0){
      return -1;
    }
  
    return q;
  }
  
  /** CHAT GPT USED TO FIND NUMBER OF THREATS */


  // ignores any queens in the specified row
  function findNumberOfThreats(arrBoard, row, col) {
    var n = arrBoard.length;
    var threats = 0;
  
    // find any queens in the other rows of this column
    for (var r = 0; r < n; r++) {
      if (r != row && arrBoard[r][col] == 1) {
        threats++;
      }
    }
  
    // find any queens/threats on the diagonal going up-left
    for (var r = row-1, c = col-1; r >= 0 && c >=0; r--, c--) {
      if (r != row && arrBoard[r][c] == 1) {
        threats++;
      }
    }
  
  // find any queens/threats on the diagonal going up-right
  for (var r = row - 1, c = col + 1; r >= 0 && c < n; r--, c++) {
    if (arrBoard[r][c] == 1) {
      threats++;
    }
  }

  // find any queens/threats on the diagonal going down-left
  for (var r = row + 1, c = col - 1; r < n && c >= 0; r++, c--) {
    if (arrBoard[r][c] == 1) {
      threats++;
    }
  }

  // find any queens/threats on the diagonal going down-right
  for (var r = row + 1, c = col + 1; r < n && c < n; r++, c++) {
    if (arrBoard[r][c] == 1) {
      threats++;
    }
  }
  
    return threats;
  
  }
  
  // function findLeastThreatenedColumn(arrBoard, q) {
  //   var n = arrBoard.length;
  //   row=q[0];
  //   col=q[1];
  
  //   var colPos = -1;
  //   var minThreats = n + 1; // initialize to max value +1
  
  
  //   return colPos;
  // }

  
  /** CHAT GPT USED TO FIND LEAST THREATEND COLUMN FOR MOST THREATEND QUEEN */

  function findLeastThreatenedColumn(arrBoard, q) {
    var n = arrBoard.length;
    var row = q[0];
    var col = q[1];

    var minThreats = n + 1;
    var colPos = -1; 

    for (var c = 0; c < n; c++) {
        if (c === col) {
            continue;
        }

        arrBoard[row][col] = 0; 
        arrBoard[row][c] = 1; 

        var threats = findNumberOfThreats(arrBoard, row, c);

        if (threats < minThreats) {
            minThreats = threats;
            colPos = c;
        }

        arrBoard[row][c] = 0; 

  

    }
    arrBoard[row][col] = 0; 

    arrBoard[row][colPos] = 1; 


    return colPos;
}
  
  