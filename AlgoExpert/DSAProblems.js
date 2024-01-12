function* factorial(n) {
    if (n<2) return 1;
    let val = 1;
    for (let i = 1; i <= n; i++) {
        val *= i;
        yield val;
    }
};
//Starting a new page as I go at all the problems again.
