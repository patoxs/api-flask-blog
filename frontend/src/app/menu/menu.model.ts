export class MenuModel {
  constructor(public url: string, public name: string, public submenu: MenuModel[]) {}
}
