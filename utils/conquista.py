from winotify import Notification
toast = Notification(app_id="Masmorra do Fim",
                     title="Conquista",
                     msg="Descobriu o autor original da peça.",
                     icon=r"C:\Pasta Dev\Masmorra_fim\utils\conquista.png")
toast.show()