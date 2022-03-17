/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
 var kClosest = function(points, k) {
    const ds = []
    const result = []
    points.forEach((p,key)=>{
        const d = Math.sqrt((p[0]**2) + (p[1]**2))
        ds[key] = {d,key}
    });
    
    ds.sort(function(x,y){
        return x.d - y.d
    }).slice(0,k).forEach(d=>{
        result.push(points[d.key])
    })
    return result
};