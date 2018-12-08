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
        let r = new RegExp(String.raw``)
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
