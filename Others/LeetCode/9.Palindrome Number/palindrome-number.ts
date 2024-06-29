function isPalindrome(x: number): boolean {
    let input_num = x;
    if (input_num < 0 || (input_num != 0 && input_num % 10 == 0)) 
        return false;
    let reversed_num = 0;
    while (input_num > reversed_num) {
        reversed_num = reversed_num * 10 + input_num % 10;
        input_num = Math.floor(input_num / 10);
    }
    return input_num == reversed_num || input_num == Math.floor(reversed_num / 10);
};