import { Component } from '@angular/core';
import { Animal } from './animal';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'material-prod';

  animals : Animal[] = [{
    name: 'Soos', type: 'Affe'
  }]   
  // List of Animals of class Animal

}
