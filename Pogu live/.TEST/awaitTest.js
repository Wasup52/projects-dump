async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function test1() {
    await sleep(1000);

    console.log('test1');
}

async function test2() {
    await test1();

    console.log('test2');
}

async function test3() {
    await test2();
    console.log('test2 then');
};

for (var i = 0; i < 10; i++) {
    test3();
    console.log('test3');
}