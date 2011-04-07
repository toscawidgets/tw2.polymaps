function setupPolymap(args,
        arrow, compass, dblclick, drag, grid, hash, interact, wheel
        ) {
        console.log(args)
        var po = org.polymaps;
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
        
        if ( arrow ) { map.add(po.arrow()); }
        if ( compass ) { map.add(po.compass()); }
        if ( dblclick ) { map.add(po.dblclick()); }
        if ( drag ) { map.add(po.drag()); }
        if ( grid ) { map.add(po.grid()); }
        if ( hash ) { map.add(po.hash()); }
        if ( interact ) { map.add(po.interact()); }
        if ( wheel ) { map.add(po.wheel()); }

}
