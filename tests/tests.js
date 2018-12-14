describe('Server Environment Variables', function() {
    const SERVER = Date.now();
    it('fails on missing data', function() {
        return request(`PUT /server/${SERVER}/env`,{}).then(response => {
            chai.expect(response.status).to.equal(400);
        })
    });
    it('fails on incorrect keys', function() {
        return request(`PUT /server/${SERVER}/env`,{"a":"6","b":"6"}).then(response => {
            chai.expect(response.status).to.equal(400);
        })
    });
    it('fails on one missing field', function() {
        return request(`PUT /server/${SERVER}/env`,{"key":"6"}).then(response => {
            chai.expect(response.status).to.equal(400);
        })
    });
    it('fails on incorrect types', function() {
        return request(`PUT /server/${SERVER}/env`,{"key":6,"value":"6"}).then(response => {
            chai.expect(response.status).to.equal(400);
        })
    });
    it('fails on incorrect key format', function() {
        return request(`PUT /server/${SERVER}/env`,{"key":"hello world","value":"6"}).then(response => {
            chai.expect(response.status).to.equal(400);
        })
    });
    it('fails on empty key', function() {
        return request(`PUT /server/${SERVER}/env`,{"key":"","value":"6"}).then(response => {
            chai.expect(response.status).to.equal(400);
        })
    });
    it('returns empty object for non existant server', function() {
        return request(`GET /server/lmao/env`)
        .then(r=>r.json())
        .then(r=>chai.expect(Object.keys(r).length).to.equal(0))
    });
    it('allows for new key value pair', function() {
        return request(`PUT /server/${SERVER}/env`,{"key":"A","value":"1"}).then(response => {
            chai.expect(response.status).to.equal(200);
        })
    });
    it('correctly stores key value pair', function() {
        return request(`GET /server/${SERVER}/env`)
        .then(r=>r.json())
        .then(r=>chai.expect(r.A).to.equal("1"))
    });
    it('allows for key to be updated', function() {
      return request(`PUT /server/${SERVER}/env`,{"key":"A","value":"2"}).then(response => {
          chai.expect(response.status).to.equal(200);
      })
    });
    it('correctly registers update', function() {
        return request(`GET /server/${SERVER}/env`)
        .then(r=>r.json())
        .then(r=>chai.expect(r.A).to.equal("2"))
    });
});
describe('Bot tests - core', function() {
    it('!hp help',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('Hodge Podge help',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('hodge podge help',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('hodgepodge help',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('hodge podge help',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('<@!431280056468242435> help',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('!hp help',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('!hp docs',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('!hp show documentation',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('!hp how do i use the core module',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('!hp how do i use anything',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('!hp how do i',function(){
        let r = new RegExp(String.raw`\[btf\] I have a nice list of what i can do at http://zainafzal08\.github\.io/HodgePodge/docs\.html`)
        chai.expect("[btf] I have a nice list of what i can do at http://zainafzal08.github.io/HodgePodge/docs.html").to.match(r);
    });
    it('!hp set a lol to b',function(){
        let r = new RegExp(String.raw`^$`)
        chai.expect("").to.match(r);
    });
    it('!hp set real_var to ha',function(){
        let r = new RegExp(String.raw`Got it!`)
        chai.expect("[btf] Got it!").to.match(r);
    });
    it('!hp set real_var to ha space',function(){
        let r = new RegExp(String.raw`Got it!`)
        chai.expect("[btf] Got it!").to.match(r);
    });
    it('!hp reveal real_var',function(){
        let r = new RegExp(String.raw`ha space`)
        chai.expect("[btf] real_var = ha space").to.match(r);
    });
});
describe('Bot tests - dice', function() {
    it('!hp roll a d2',function(){
        let r = new RegExp(String.raw`(^\[btf\] oof\. I got [12]!$)|(^\[btf\] I got [12]! Nice!$)`)
        chai.expect("[btf] I got 2! Nice!").to.match(r);
    });
    it('!hp roll a d20',function(){
        let r = new RegExp(String.raw`(^\[btf\] I got ([12][0-9]|[1-9])!$)|(^\[btf\] oof. I got 1!$)|(^\[btf\] I got 20! Nice!$)`)
        chai.expect("[btf] I got 2!").to.match(r);
    });
    it('!hp roll a d10001',function(){
        let r = new RegExp(String.raw`\[btf\] How can you even have that many faces on a dice\? Pick a reasonable dice please!`)
        chai.expect("[btf] How can you even have that many faces on a dice? Pick a reasonable dice please!").to.match(r);
    });
    it('!hp roll a d1',function(){
        let r = new RegExp(String.raw`\[btf\] How can you even have that many faces on a dice\? Pick a reasonable dice please!`)
        chai.expect("[btf] How can you even have that many faces on a dice? Pick a reasonable dice please!").to.match(r);
    });
    it('!hp roll a d0',function(){
        let r = new RegExp(String.raw`\[btf\] How can you even have that many faces on a dice\? Pick a reasonable dice please!`)
        chai.expect("[btf] How can you even have that many faces on a dice? Pick a reasonable dice please!").to.match(r);
    });
    it('!hp roll a d-1',function(){
        let r = new RegExp(String.raw`^$`)
        chai.expect("").to.match(r);
    });
    it('!hp roll a d2 +1',function(){
        let r = new RegExp(String.raw`(^\[btf\] oof\. I got 2 \[1\+1\]!$)|(^\[btf\] I got 3 \[2\+1\]! Nice!$)`)
        chai.expect("[btf] I got 3 [2+1]! Nice!").to.match(r);
    });
    it('!hp roll a d2 -1',function(){
        let r = new RegExp(String.raw`(^\[btf\] oof\. I got 0 \[1\-1\]!$)|(^\[btf\] I got 1 \[2\-1\]! Nice!$)`)
        chai.expect("[btf] I got 1 [2-1]! Nice!").to.match(r);
    });
    it('!hp roll a d2 +100001',function(){
        let r = new RegExp(String.raw`Bit of a intense modifier, not sure i can handle a number like that\. Sorry!`)
        chai.expect("[btf] Bit of a intense modifier, not sure i can handle a number like that. Sorry!").to.match(r);
    });
    it('!hp roll a d2 -100001',function(){
        let r = new RegExp(String.raw`Bit of a intense modifier, not sure i can handle a number like that\. Sorry!`)
        chai.expect("[btf] Bit of a intense modifier, not sure i can handle a number like that. Sorry!").to.match(r);
    });
    it('!hp set critical_hit_msg to B',function(){
        let r = new RegExp(String.raw`Got it!`)
        chai.expect("[btf] Got it!").to.match(r);
    });
    it('!hp set critical_miss_msg to A',function(){
        let r = new RegExp(String.raw`Got it!`)
        chai.expect("[btf] Got it!").to.match(r);
    });
    it('!hp roll a d2',function(){
        let r = new RegExp(String.raw`(^\[btf\] A I got [12]!$)|(^\[btf\] I got [12]! B$)`)
        chai.expect("[btf] A I got 1!").to.match(r);
    });
    it('!hp roll a d2',function(){
        let r = new RegExp(String.raw`(^\[btf\] A I got [12]!$)|(^\[btf\] I got [12]! B$)`)
        chai.expect("[btf] I got 2! B").to.match(r);
    });
    it('!hp roll a d2',function(){
        let r = new RegExp(String.raw`(^\[btf\] A I got [12]!$)|(^\[btf\] I got [12]! B$)`)
        chai.expect("[btf] I got 2! B").to.match(r);
    });
    it('!hp roll a d2',function(){
        let r = new RegExp(String.raw`(^\[btf\] A I got [12]!$)|(^\[btf\] I got [12]! B$)`)
        chai.expect("[btf] A I got 1!").to.match(r);
    });
    it('!hp reroll',function(){
        let r = new RegExp(String.raw`(^\[btf\] A I got [12]!$)|(^\[btf\] I got [12]! B$)`)
        chai.expect("[btf] A I got 1!").to.match(r);
    });
    it('!hp set critical_hit_msg to Nice!',function(){
        let r = new RegExp(String.raw`Got it!`)
        chai.expect("[btf] Got it!").to.match(r);
    });
    it('!hp set critical_miss_msg to oof.',function(){
        let r = new RegExp(String.raw`Got it!`)
        chai.expect("[btf] Got it!").to.match(r);
    });
    it('!hp roll 1 d5',function(){
        let r = new RegExp(String.raw`I got [1-5]! The breakdown was \([1-5]\)`)
        chai.expect("[btf] I got 1! The breakdown was (1)").to.match(r);
    });
    it('!hp roll 5 d5',function(){
        let r = new RegExp(String.raw`I got (2[0-5])|(1[0-9])|([1-9])! The breakdown was \(([1-5],){4}[1-5]\)`)
        chai.expect("[btf] I got 19! The breakdown was (3,4,3,4,5)").to.match(r);
    });
    it('!hp roll 21 d5',function(){
        let r = new RegExp(String.raw`^\[btf\] I got \d+!$`)
        chai.expect("[btf] I got 63!").to.match(r);
    });
    it('!hp roll 2 d2',function(){
        let r = new RegExp(String.raw`^\[btf\] I got [234]! The breakdown was \([12],[12]\)$`)
        chai.expect("[btf] I got 3! The breakdown was (1,2)").to.match(r);
    });
    it('!hp reroll',function(){
        let r = new RegExp(String.raw`^\[btf\] I got [234]! The breakdown was \([12],[12]\)$`)
        chai.expect("[btf] I got 4! The breakdown was (2,2)").to.match(r);
    });
    it('!hp roll 2 d3 ++1',function(){
        let r = new RegExp(String.raw`I got [4-8]! The breakdown was \([1-3]\[\+1\],[1-3]\[\+1\]\)`)
        chai.expect("[btf] I got 8! The breakdown was (3[+1],3[+1])").to.match(r);
    });
    it('!hp roll 2 d3 +1',function(){
        let r = new RegExp(String.raw`I got [3-7]! The breakdown was \([1-3],[1-3]\)\[\+1\]`)
        chai.expect("[btf] I got 4! The breakdown was (2,1)[+1]").to.match(r);
    });
});
describe('Bot tests - hodgecode', function() {
    it('!hp do 1+1',function(){
        let r = new RegExp(String.raw`2`)
        chai.expect("[btf] 2").to.match(r);
    });
    it('!hp do 1+1-1+1-1',function(){
        let r = new RegExp(String.raw`1`)
        chai.expect("[btf] 1").to.match(r);
    });
    it('!hp do 234+1',function(){
        let r = new RegExp(String.raw`235`)
        chai.expect("[btf] 235").to.match(r);
    });
    it('!hp do 1.0+1',function(){
        let r = new RegExp(String.raw`2`)
        chai.expect("[btf] 2").to.match(r);
    });
    it('!hp do 1.0+2.0',function(){
        let r = new RegExp(String.raw`3`)
        chai.expect("[btf] 3").to.match(r);
    });
    it('!hp do 1+1*2-9*1+2-123',function(){
        let r = new RegExp(String.raw`-127`)
        chai.expect("[btf] -127").to.match(r);
    });
    it('!hp do 1+1*2-9/1+2-123',function(){
        let r = new RegExp(String.raw`-127`)
        chai.expect("[btf] -127").to.match(r);
    });
    it('!hp do 1/2',function(){
        let r = new RegExp(String.raw`0.5`)
        chai.expect("[btf] 0.5").to.match(r);
    });
    it('!hp do 1/3',function(){
        let r = new RegExp(String.raw`0.33333333`)
        chai.expect("[btf] 0.33333333").to.match(r);
    });
    it('!hp do 1.0/3',function(){
        let r = new RegExp(String.raw`0.33333333`)
        chai.expect("[btf] 0.33333333").to.match(r);
    });
    it('!hp do 0',function(){
        let r = new RegExp(String.raw`0`)
        chai.expect("[btf] 0").to.match(r);
    });
    it('!hp do 1.0',function(){
        let r = new RegExp(String.raw`1`)
        chai.expect("[btf] 1").to.match(r);
    });
    it('!hp do 3',function(){
        let r = new RegExp(String.raw`3`)
        chai.expect("[btf] 3").to.match(r);
    });
    it('!hp do 100+0',function(){
        let r = new RegExp(String.raw`100`)
        chai.expect("[btf] 100").to.match(r);
    });
    it('!hp do 100+d2',function(){
        let r = new RegExp(String.raw`10[12]`)
        chai.expect("[btf] 101").to.match(r);
    });
    it('!hp do d3',function(){
        let r = new RegExp(String.raw`[123]`)
        chai.expect("[btf] 1").to.match(r);
    });
    it('!hp do d8+2-1',function(){
        let r = new RegExp(String.raw`[2-9]`)
        chai.expect("[btf] 3").to.match(r);
    });
    it('!hp do d2*4',function(){
        let r = new RegExp(String.raw`[48]`)
        chai.expect("[btf] 4").to.match(r);
    });
    it('!hp do d2/2',function(){
        let r = new RegExp(String.raw`1|(0\.5)`)
        chai.expect("[btf] 0.5").to.match(r);
    });
});
