from flet import*

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'


    def shrink(e):
        page_2.controls[0].width=120
        page_2.controls[0].scale=transform.Scale(
            0.8, alignment=alignment.center_right
        )

        
        page_2.update()
    def restore(e):
        page_2.controls[0].width=400
        page_2.controls[0].scale=transform.Scale(
            1, alignment=alignment.center_right
        )
        page_2.update()

    prod_venc=Row(
        scroll='auto'

    )
    tiempo=['menos de una semana', '1semana','2semanas']
    for f, i in enumerate(tiempo):
        prod_venc.controls.append(
            Container(
                bgcolor=BG,
                height=110,
                width=170,
                border_radius=20,
                padding=15,
                #agrega contenido alos recuadros de productos por vencer
                content=Column(
                    controls=[
                        Text('Tiempo de vencimiento:'),
                        Text(i),
                        Container(
                            width=160,
                            height=40,
                            bgcolor='white12',
                            border_radius=10,
                            padding=padding.only(right=f*30),
                            content=Container(
                                bgcolor=PINK,
                            )
                        )

                    ]
                    
                )
            )
        )
    
    prod_reabastecer=Row(
        scroll='auto'

    )
    cantidad=['menos de n cantidad', 'ncantidad','ncantidad']
    for f, i in enumerate(cantidad):
        prod_reabastecer.controls.append(
            Container(
                bgcolor=BG,
                height=110,
                width=170,
                border_radius=20,
                padding=15,
                #agrega contenido alos recuadros de productos por vencer
                content=Column(
                    controls=[
                        Text('CANTIDAD EN INVENTARIO:'),
                        Text(i),
                        Container(
                            width=160,
                            height=40,
                            bgcolor='white12',
                            border_radius=10,
                            padding=padding.only(right=f*30),
                            content=Container(
                                bgcolor=PINK,
                            )
                        )

                    ]
                    
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
               
                    controls=[
                        Container(on_click=lambda e: shrink(e),  # Cambié "container" por "Container"
                            content=Icon(
                                icons.MENU
                            )
                        ),
                        Row(
                            controls=[
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ],
                        ),
                    ],
                ),
                Text(
                    value='INICIO'
                ),
                Text(
                    value='PRODUCTOS POR VENCER'
                ),
                Container(
                    padding=padding.only(top=10,bottom=20,),
                    content=prod_venc
                ),
                Container(height=10),
                Text("PRODUCTOS POR REABASTECER"),
                Stack(
                    controls=[
                        Container(
                            padding=padding.only(top=10,bottom=20,),
                            content=prod_reabastecer
                        ),

                        #FloatingActionButton()

                    ],
                ),
                
            ],
        ),
    )

    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50,top=60,right=200),

        content=Column(
            controls=[
                Row(alignment='end',
                    controls=[
                        Container(border_radius=25,padding=padding.only(top=3, left=3),
                            height=50, width=50,border=border.all(color='white',width=1),
                            on_click=lambda e: restore(e),
                            content=Text('<')
                        )

                        
                    ]
                ),
                Text('MENU DE \nOPCIONES',size=25,weight='bold'),



            ]
        )
    )
    
    page_2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                    left=20, top=50, right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ],
                ),
            ),
        ],
    )
    container=Container(
        width=400, 
        height=850, 
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    page.add(container)

app(target=main)