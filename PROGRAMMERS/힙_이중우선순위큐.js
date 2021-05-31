function solution(operations) {
  let problem = operations
  let answer = [];

  let result = [];

  for (let i = 0; i < problem.length; i++) {
    if (result && problem[i] === 'D 1') {
      result.pop()
    } else if (result && problem[i] === 'D -1') {
      result.shift()
    } else {
      let a = problem[i].split(' ');
      let num = parseInt(a[1])
      result.push(num)
      console.log(result)
      result.sort(function(a, b) {
        return a - b
      })
    }
  }
  if (result.length > 1) {
    answer = [result[result.length-1], result[0]]
  } else {
    answer = [0,0]
  }

  return answer;
}


console.log(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
