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
