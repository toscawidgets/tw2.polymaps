
var po = org.polymaps;

function setupPolymap(args)
{
        var map = po.map();
        map.container(
                document.getElementById(args.id+":target")
                .appendChild(po.svg("svg"))
        );

        // http://cloudmade.com/register
        map.add(po.image()
        .url(po.url("http://{S}tile.cloudmade.com"
                + "/1a1b06b230af4efdbb989ea99e9841af"
                + "/999/256/{Z}/{X}/{Y}.png")
                .hosts(["a.", "b.", "c.", ""])));
        return map;
}

function setupPolymapControls(
        map, arrow, compass, dblclick, drag,
        grid, hash, interact, wheel)
{
        if ( arrow ) { map.add(po.arrow()); }
        if ( compass ) { map.add(po.compass()); }
        if ( dblclick ) { map.add(po.dblclick()); }
        if ( drag ) { map.add(po.drag()); }
        if ( grid ) { map.add(po.grid()); }
        if ( hash ) { map.add(po.hash()); }
        if ( interact ) { map.add(po.interact()); }
        if ( wheel ) { map.add(po.wheel()); }
        return map;
}

function setupPolymapData(map, data_url)
{
        if ( data_url ) {
                map.add(
                        po.geoJson()
                        .url(data_url)
                );
        }
}

function setupPolymapPollingData(map, data_url, interval)
{
        if ( data_url ) {
                var layer = po.geoJson().url(data_url)
                map.add(layer);
                setInterval( function () {
                        layer.url(data_url);
                }, interval );
        }
}
